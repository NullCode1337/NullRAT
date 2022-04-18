using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using NullRAT.Variables;
using Spectre.Console;

internal class VariablesPY
{
    internal static bool GetServerIDs(ref RATVariables NullratVars)
    {
        int success = 0;
        ulong tResult = 0;
        string[] serverIDs;
        StringBuilder serverIDCollection = new();
        AnsiConsole.MarkupLine("\n[white]([/][yellow]Example:[/] [white]937923464709414922[yellow],[/]422814981520621569)[/]");

        serverIDCollection.Append(
            AnsiConsole.Prompt(
                new TextPrompt<string>("[white]Enter the [/][yellow]server IDs[/] [maroon]with commas:[/] ")
                    .PromptStyle("white")));

        if (serverIDCollection.ToString().Contains(','))
            serverIDs = serverIDCollection.ToString().Split(',');
        else
            serverIDs = serverIDCollection.ToString().Split(' ');

        for (int i = 0; i < serverIDs.Length; i++)
        {
            if (!ulong.TryParse(serverIDs[i], out tResult) || tResult.ToString().Length != 18)
            {
                AnsiConsole.MarkupLine($"[red1]\nServer ID(s) N{i + 1} is invalid!\n[/]");
                serverIDCollection.Clear();
            }
            else
            {
                NullratVars.Server_IDs.Add(tResult);
                success++;
            }
        }
        return success == serverIDs.Length; // Return true or false.
    }
    internal static bool GetNotificationId(ref RATVariables NullratVars)
    {
        ulong tResult = 0;
        StringBuilder notifCnnId = new();

        notifCnnId.Append(AnsiConsole.Prompt(
        new TextPrompt<string>("[white]Enter the [/][yellow]channel ID:[/] ")
            .PromptStyle("white")));

        if (!ulong.TryParse(notifCnnId.ToString(), out tResult) || tResult.ToString().Length != 18)
        {
            AnsiConsole.MarkupLine("[red1]\nA Channel ID doesn't have letters or special characters and has to be 18 chars long!\n[/]");
            return false;
        }
        else
        {
            NullratVars.Notification_Channel_ID = tResult;
            return true;
        }
    }
    internal static bool GetToken(ref RATVariables NullratVars)
    {
        Regex tokenRegex = new(
        @"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",
        RegexOptions.Compiled | RegexOptions.IgnoreCase
            );
        StringBuilder token = new();
        token.Append(
        AnsiConsole.Prompt(new TextPrompt<string>("[white]Enter the[/] [yellow]bot token: [/]")
            .PromptStyle("white")
            .Secret()));

        if (!tokenRegex.IsMatch(token.ToString()))
        {
            AnsiConsole.MarkupLine("[red1]\nInvalid token!\n[/]");
            return false;
        }
        else
        {
            NullratVars.Bot_Token = token;
            return true;
        }
    }
}