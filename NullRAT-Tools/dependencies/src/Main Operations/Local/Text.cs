using Spectre.Console;
using System;
using System.Threading;

namespace NullRAT.Dependencies;
public static class Text
{
    public static readonly Object slowPrintLock = new();
    /// <summary>
    /// Prints text in the center of the Console
    /// </summary>
    /// <param name="Text">The Text to print</param>
    /// <param name="Color">The color to use, red1, green1...</param>
    public static void CenterText(string Text, string Color)
    {
        for (int i = 0; i < (Console.WindowWidth - Text.Length) / 2; i++)
        {
            Console.Write(' ');
        }
        AnsiConsole.MarkupLine($"[{Color}]{Text}[/]");
    }
    /// <summary>
    /// Print the text with [[INFO]] at the start with 0.025 seconds of retard
    /// </summary>
    /// <param name="Text">The Text to print</param>
    /// <param name="Color">The color to use, red1, green1...</param>
    /// <param name=="newLine">true if you want the code to add a NewLine at the end</param>
    public static void SlowPrintI(string Text, string Color, bool newLine)
    {
        lock (slowPrintLock)
        {
            AnsiConsole.Markup($"[{Color}][[INFO]][/] ");
            for (int i = 0; i < Text.Length; i++)
            {
                AnsiConsole.Markup($"[{Color}]{Text[i]}[/]");
                Thread.Sleep(25);
            }
            if (newLine)
            {
                Console.Write($"{Environment.NewLine}");
            }
        }
    }
    /// <summary>
    /// Print the text with 0.025 seconds of retard
    /// </summary>
    /// <param name="Text">The Text to print</param>
    /// <param name="Color">The color to use, red1, green1...</param>
    public static void SlowPrint(string Text, string Color, bool SkipLine)
    {
        lock (slowPrintLock)
        {
            for (int i = 0; i < Text.Length; i++)
            {
                AnsiConsole.Markup($"[{Color}]{Text[i]}[/]");
                Thread.Sleep(25);
            }
            if (SkipLine)
            {
                AnsiConsole.Markup($"{Environment.NewLine}");
            }
        }
    }
}