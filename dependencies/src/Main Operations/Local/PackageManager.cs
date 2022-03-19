using System;
using Spectre.Console;
using System.Threading;
using System.Linq;
using System.Threading.Tasks;

namespace NullRAT.Dependencies;
internal class PackageManager
{
    /// <summary>
    /// Install a PIP Package
    /// </summary>
    /// <param name="PackageName">The name of the package</param>
    /// <exception cref="Exception">Thrown when the package couldn't be installed successfully</exception>
    public async Task InstallPipPackage(string PackageName)
    {
        Task<CmdOutput> pipTask;
        CmdOutput cmdOutput = new();

        if (ProgramData.PipPackageList.Contains(PackageName))
        {
            Text.SlowPrintI($"{PackageName} is installed!", "green", true);
            ProgramData.InstalledPackages++;
        }
        else
        {
            string pipInstallCommand = $"pip install --no-input --user {PackageName}";

            lock (Text.slowPrintLock)
            {
                AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PackageName} not installed![/]");
            }
            Thread.Sleep(1000);

            Text.SlowPrintI($"Installing {PackageName}...", "orange1", true);

            pipTask = Task<CmdOutput>.Run(
                    () => ProcessInvoker.RunCmd("python", $"-m {pipInstallCommand}"));

            while (true) {
                if (pipTask.IsCompleted) {
                    cmdOutput = pipTask.Result;
                    break;
                }
                await Task.Delay(500);
            }

            if (cmdOutput.ExitCode is not 0 && cmdOutput.ExitCode is not 1)
            {
                AnsiConsole.MarkupLine($"[maroon][[ERROR]] Error Installing {PackageName}. Pip exit code \"{cmdOutput.ExitCode}\" does not indicate success!\nTry installing it with: [orange1]{pipInstallCommand}[/][/]");
                ProgramData.PackagesFailed++;
                ProgramData.FailedPackages.Add(PackageName);
                AnsiConsole.MarkupLine($"--------PIP OUTPUT\n{cmdOutput.Output?.ToString().RemoveMarkup()}\n--------END OUTPUT");
            }
            else
            {
                Text.SlowPrintI($"{PackageName} has been successfully installed!", "green", true);
            }
            ProgramData.InstalledPackages++;
        }
    }
    /// <summary>
    /// Removes a PIP Package
    /// </summary>
    /// <param name="pipPackageName">The name shown in <s>PIP freeze</s> of the package to uninstall</param>
    public void RemovePipPackage(string PackageName)
    {
        for (var i = 0; i < ProgramData.PipPackageList.Length; i++)
        {
            if (ProgramData.PipPackageList[i].Equals(PackageName))
            {
                AnsiConsole.MarkupLine($"[yellow][[INFO]] Uninstalling [red bold]{PackageName}[/]...[/]");
                string pipInstallCommand = $"pip uninstall --no-input -y {PackageName}";

                if (ProcessInvoker.RunCmd("python", $"-m {pipInstallCommand}").ExitCode is not 0)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] An error ocurred while the installer tried to uninstall [red bold]{PackageName}[/]. Please, run [red]{pipInstallCommand}[/] manually to uninstall the conflicting package.[/]");
                    throw new InvalidOperationException($"Unable to uninstall package! Error at -> {this.GetType()}");
                }
                else
                {
                    AnsiConsole.MarkupLine($"[green][[INFO]] [red bold]{PackageName}[/] was uninstalled successfully.[/]");
                    break;
                }
            }
        }
    }
}