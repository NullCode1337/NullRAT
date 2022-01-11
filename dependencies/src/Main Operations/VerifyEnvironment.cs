namespace NullCode.Dependencies
{
    internal class VerifyEnvironment
    {
		/// <summary>
		/// Verifies PIP and Python, and gets the currently installed packages
		/// </summary>
        public static void VerifyPipAndPython()
        {
			//Get Env Var path, and checks if there is a path with "Python" in it, if it isn't execute if.
			if (ProcessInvoker.RunCmd("python", "--version").ExitCode != 0)
			{
				AnsiConsole.MarkupLine(ProgramData.noPython2);
				AnsiConsole.MarkupLine(ProgramData.noPython);
				Thread.Sleep(4500);
				Environment.Exit(2);
			}


			//Check if PIP is working.
			CmdOutput cOut = ProcessInvoker.RunCmd("pip", "freeze");


			if (cOut.ExitCode == 0)
			{
				string[] tmp = cOut.Output.ToString().Split(Environment.NewLine);

                for (int i = 0; i < tmp.Length; i++)
                {
					ProgramData.PipPackageList.Append(tmp[i]);
                }
				
				AnsiConsole.MarkupLine("\n[green][[INFO]] PIP is working![/]");
			}
		}
    }
}
