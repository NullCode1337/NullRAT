namespace NullRAT.Dependencies
{
    internal class VerifyEnvironment
    {
        /// <summary>
        /// Verifies PIP and Python, and gets the currently installed packages
        /// </summary>
        public static void VerifyPipAndPython()
        {
            #region Verify Python
            if (ProcessInvoker.RunCmd("python", "--version").ExitCode != 0)
            {
                AnsiConsole.MarkupLine(ProgramData.noPython2);
                AnsiConsole.MarkupLine(ProgramData.noPython);
                Thread.Sleep(4500);
                Environment.Exit(2);
            } 
            else
            {
                Text.SlowPrintI("Python is installed!", "green", true);
            }

            #endregion
            #region Verify Pip
            //Check if PIP is working.
            CmdOutput fOut = ProcessInvoker.RunCmd("python", "-m pip freeze");

            if (fOut.ExitCode == 0)
            {
                string[] tmp = fOut.Output.ToString().Split(Environment.NewLine);

                for (int i = 0; i < tmp.Length; i++)
                {
                    ProgramData.PipPackageList.Append(tmp[i]);
                }

                Text.SlowPrintI("PIP is available!", "green", true);
            }
            #endregion
            #region Verify Wheel
            CmdOutput wOut = ProcessInvoker.RunCmd("python", " -m wheel version");

            //
            if (wOut.ExitCode == 0)
            {
                Text.SlowPrintI("Wheel is installed!", "green", true);
            } 
            else
            {
                AnsiConsole.MarkupLine("[maroon][[WARN]] wheel isn't installed![/]");
                Text.SlowPrintI("Installing wheel...", "orange1", true);
                ProcessInvoker.RunCmd("pip", " install wheel");
            }
            #endregion
        }
    }
}
