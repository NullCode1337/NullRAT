namespace NullCode.Dependencies
{
    public class Text
    {
		/// <summary>
		/// Prints text in the center of the Console
		/// </summary>
		/// <param name="Text">The Text to print</param>
		/// <param name="Color">The color to use, red1, green1...</param>
		public static void CenterText(string Text, string Color)
		{
			for (int i = 0; i < (Console.WindowWidth - Text.Length) / 2; i++)
			{
				Console.Write(" ");
			}
			AnsiConsole.MarkupLine($"[{Color}]{Text}[/]");
		}
		/// <summary>
		/// Print the text with 0.025 seconds of retard
		/// </summary>
		/// <param name="Text">The Text to print</param>
		/// <param name="Color">The color to use, red1, green1...</param>
		public static void SlowPrint(string Text, string Color)
		{
            for (int i = 0; i < Text.Length; i++)
            {			
				AnsiConsole.Markup($"[{Color}]{Text[i]}[/]");
				Thread.Sleep(25);
			}
		}
	}
}
