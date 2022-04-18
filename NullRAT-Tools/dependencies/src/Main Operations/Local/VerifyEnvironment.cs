using System.Threading;
using System.Text;
using System.Collections.Generic;
using Spectre.Console;
using System.Threading.Tasks;
using System;

namespace NullRAT.Dependencies;
internal static class VerifyEnvironment
{
    /// <summary>
    /// Verifies Basic Environment needs, Python, Pip and Wheel.
    /// </summary>
    public static async Task VerifyBasic()
    {
        Task? processPackageList, wheelInstall = null;
        #region Verify Python
        if (ProcessInvoker.RunCmd("python", "--version").ExitCode is not 0) {
            AnsiConsole.MarkupLine(ProgramData.noPython2);
            AnsiConsole.MarkupLine(ProgramData.noPython);
            Thread.Sleep(4500);
            Environment.Exit(2);
        } else {
            Text.SlowPrintI("Python is installed!", "green", true);
        }

        #endregion
        #region Verify Pip

        CmdOutput fOut = ProcessInvoker.RunCmd("python", "-m pip freeze");

        if (fOut.ExitCode is 0) {
            string[] preProcessed = fOut.Output.ToString().Split(Environment.NewLine);

            processPackageList = Task.Run(() =>
            {
                List<string> processed = new();
                for (int i = 0; i < preProcessed.Length; i++)
                {
                    processed.Add(preProcessed[i].Split('=')[0]); // Split to only get the package names.
                }
                ProgramData.PipPackageList = processed.ToArray();
            });

            Text.SlowPrintI("PIP is installed!", "green", true);
        } else {
            Text.SlowPrintI("PIP is not installed or is broken!", "red", true); // Warn about Pip being f up!
            throw new InvalidProgramException("PIP is not installed or is broken! Please reinstall PIP."); // Throw ex.
        }
        #endregion

        #region Verify Wheel

        if (ProcessInvoker.RunCmd("python", " -m wheel version").ExitCode is 0) {
            Text.SlowPrintI("Wheel is installed!", "green", true);
        } else {
            AnsiConsole.MarkupLine("[maroon][[WARN]] wheel isn't installed![/]");
            wheelInstall = Task.Run(() => ProcessInvoker.RunCmd("python", "-m pip install --no-input --user wheel"));
            Text.SlowPrintI("Installing wheel...", "orange1", true);
        }
        #endregion
        // Await Tasks if they're NOT completed yet...
        if (processPackageList?.IsCompleted is false) await processPackageList;
        if (wheelInstall?.IsCompleted is false) await wheelInstall;
    }
}
