using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using Nulllib;

namespace NullRAT.Variables;

internal static class Utils
{
    internal static void PrintNullRAT()
    {
        Text.CenterText(" ███▄    █  █    ██  ██▓     ██▓     ██▀███   ▄▄▄     ▄▄▄█████▓", "#6A66FF");
        Text.CenterText(" ██ ▀█   █  ██  ▓██▒▓██▒    ▓██▒    ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒", "#6A66FF");
        Text.CenterText("▓██  ▀█ ██▒▓██  ▒██░▒██░    ▒██░    ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░", "#6A66FF");
        Text.CenterText("▓██▒  ▐▌██▒▓▓█  ░██░▒██░    ▒██░    ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ", "#6A66FF");
        Text.CenterText("▒██░   ▓██░▒▒█████▓ ░██████▒░██████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ", "#6A66FF");
        Text.CenterText("░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▓  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ", "#6A66FF");
        Text.CenterText("░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░ ▒  ░░ ░ ▒  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░    ", "#6A66FF");
        Text.CenterText("   ░   ░ ░  ░░░ ░ ░   ░ ░     ░ ░     ░░   ░   ░   ▒    ░      ", "#6A66FF");
    }
    internal static Task<string> GetListAsString(List<ulong> listString)
    {
        StringBuilder sb = new();
        //Iterate through the amount of server ids, until it finds the end thanks to the exception, write the last line and mark the ending with a ]
        for (int i = 0; i < listString.Count; i++)
        {
            if (listString.Count - 1 == i)
            {
                sb.Append(listString[i]);
                break;
            }

            sb
              .Append(listString[i])
              .Append(", ");
        }
        return Task.Run(() => sb.ToString());
    }
    internal static async Task<RATVariables> ParseVariablesPy(string variablespyContent)
    {
        List<Task> tasks = new();

        string token = null!;
        List<ulong> srvIds = new();
        ulong notifCnn = 0;

        string[] splittedContent = variablespyContent.Split(Environment.NewLine);

        for (int i = 0; i < splittedContent.Length; i++)
        {
            if (splittedContent[i].Contains("bot_token", StringComparison.OrdinalIgnoreCase))
            {
                string a = splittedContent[i].Split('=')[1].Replace('\"', ' ');
                token = a.Trim();
            }
            else if (splittedContent[i].Contains("notification_channel", StringComparison.OrdinalIgnoreCase))
            {
                string b = splittedContent[i].Split('=')[1];
                notifCnn = ulong.Parse(b.Trim());
                Console.WriteLine(notifCnn);
            }
            else if (splittedContent[i].Contains("server_ids", StringComparison.OrdinalIgnoreCase))
            {
                string c = splittedContent[i].Split('=')[1].Replace('[', ' ').Replace(']', ' ');
                string[] individualIds = c.Split(',');

                for (int j = 0; j < individualIds.Length; j++)
                {
                    srvIds.Add(ulong.Parse(individualIds[j]));
                }
            }
        }
        while (tasks.Count > 0)
        {
            Task cmpTask = await Task.WhenAny(tasks);

            if (cmpTask.IsFaulted)
            {
                throw new InvalidDataException($"Variables.py is invalid. Task in position [[{tasks.IndexOf(cmpTask)}]] Error -> {cmpTask.Exception}");
            }
            tasks.Remove(cmpTask);
        }

        return new()
        {
            Bot_Token = new(token),
            Notification_Channel_ID = notifCnn,
            Server_IDs = srvIds
        };
    }
}