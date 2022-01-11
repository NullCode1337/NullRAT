namespace NullCode.Dependencies
{
    internal class Exit
    {
        /// <summary>
        /// The program's exit point
        /// </summary>
        public static void ExitProgram()
        {
            while(ProgramData.InstalledPackages < ProgramData.PackagesToInstall)
            {
                Console.WriteLine(ProgramData.InstalledPackages + " && " + ProgramData.PackagesToInstall);
                Thread.Sleep(500);
            }
            AnsiConsole.WriteLine();
            AnsiConsole.Write(new Rule());
            AnsiConsole.MarkupLine("\n[green][[INFO]] All Packages have been installed successfully![/]\n");

            Environment.Exit(0);
        }
    }
}
