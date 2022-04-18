using System.Text;
using System.Threading.Tasks;

namespace Nulllib;
public static class Utilities
{
    public static void PrintNullRAT()
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
    public static Task<string> GetListAsString(List<ulong> listString)
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
}
