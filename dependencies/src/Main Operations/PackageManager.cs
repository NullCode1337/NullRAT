namespace NullRAT.Dependencies
{
    internal class InstallPackage
    {
        /// <summary>
        /// Install a PIP Package
        /// </summary>
        /// <param name="PackageName">The name of the package</param>
        /// <exception cref="Exception">Thrown when the package couldn't be installed successfully</exception>
        public static void InstallPipPackage(string PackageName)
        {
            CmdOutput _cmdOutput = new();

            if (ProgramData.PipPackageList.ToString().Contains(PackageName))
            {
                Text.SlowPrintI($"{PackageName} is installed!", "green", true);
                ProgramData.InstalledPackages++;
            }
            else
            {
                string pipCommand = "pip" + $" install {PackageName}";

                lock (Text.slowPrintLock)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PackageName} not installed![/]");
                }
                Thread.Sleep(1000);

                Text.SlowPrintI($"Installing {PackageName}...", "orange1", true);

                Thread VirtualEnvInstaller = new(
                    () => _cmdOutput = ProcessInvoker.RunCmd("python", $"-m pip install {PackageName} --user", "y")
                    );

                VirtualEnvInstaller.Start();


                while (VirtualEnvInstaller.IsAlive)
                {
                    Thread.Sleep(5);
                }

                if (_cmdOutput.ExitCode != 0 && _cmdOutput.ExitCode != 1)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] Error Installing {PackageName}. Pip exit code \"{_cmdOutput.ExitCode}\" does not indicate success!\nTry installing it with: [orange1]{pipCommand}[/][/]");
                    ProgramData.PackagesFailed++;
                    AnsiConsole.MarkupLine($"--------PIP OUTPUT\n{_cmdOutput.Output.ToString().RemoveMarkup()}\n--------END OUTPUT");
                }
                else
                {
                    Text.SlowPrintI($"{PackageName} has been successfully installed!", "green", true);
                }
                ProgramData.InstalledPackages++;
            }
        }
        /// <summary>
        /// Install a PIP Package that comes from Git and requires "special" treatment
        /// </summary>
        /// <param name="_pipPackageName">The name of the package on Pip Freeze</param>
        /// <param name="_gitMasterLink">Link to github Repository source, must be in zip!</param>
        /// <exception cref="Exception">Thrown when the package couldn't be installed successfully</exception>
        public static void InstallPipPackage(string _pipPackageName, string _gitMasterLink)
        {
            CmdOutput _cmdOutput = new();
            string PathToPackage = Path.GetTempFileName(),
                   FinalPath = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData) + @$"/pip/local-paclages0/";

            if (ProgramData.PipPackageList.ToString().Contains(_pipPackageName))
            {
                Text.SlowPrintI($"{_pipPackageName} is installed!", "green", true);
                ProgramData.InstalledPackages++;
            }
            else
            {
                Thread.Sleep(1000);
                lock (Text.slowPrintLock)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] {_pipPackageName} not installed![/]");
                }
                Thread.Sleep(1000);
                Text.SlowPrintI($"Installing {_pipPackageName}...", "orange1", true);

                string pipCommand = "pip" + $" install ";


                Thread VirtualEnvInstaller = new(
                    () => _cmdOutput = ProcessInvoker.RunCmd("python", $"-m pip install --user \"{_gitMasterLink}\"")
                    );

                VirtualEnvInstaller.Start();

                while (VirtualEnvInstaller.IsAlive)
                {
                    Thread.Sleep(5);
                }
                if (_cmdOutput.ExitCode != 0)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] Error Installing {_pipPackageName}. Pip exit code \"{_cmdOutput.ExitCode}\" does not indicate success!\nTry running: [orange1]{pipCommand}{_gitMasterLink}[/][/]");
                    ProgramData.PackagesFailed++;
                    AnsiConsole.MarkupLine($"--------PIP OUTPUT\n{_cmdOutput.ErrorO.ToString().RemoveMarkup()}\n--------END OUTPUT");
                }
                else
                {
                    Text.SlowPrintI($"{_pipPackageName} has been successfully installed!", "green", true);
                }
                ProgramData.InstalledPackages++;
            }
        }
    }
    internal class RemovePackage
    {
        /// <summary>
        /// Removes a PIP Package
        /// </summary>
        /// <param name="fancyPackageName">The name shown in <s>PIP freeze</s> of the package to uninstall</param>
        public static void RemovePipPackage(string fancyPackageName)
        {
            string[] installedPkg = ProgramData.PipPackageList.ToString().Split('\n');
            bool pkgPresent = false;
            for (var i = 0; i < installedPkg.Length; i++)
            {
                if (installedPkg[i].Contains(fancyPackageName))
                {
                    pkgPresent = true;
                    AnsiConsole.MarkupLine($"[yellow][[INFO]] Uninstalling [red bold]{fancyPackageName}[/]...[/]");
                    break;
                }
            }
            if (pkgPresent)
            {
                string pipCommand = $"pip uninstall -y {fancyPackageName}";
                CmdOutput pipOut = ProcessInvoker.RunCmd("pip", $"uninstall --no-input -y {fancyPackageName}");

                if (pipOut.ExitCode != 0)
                {
                    AnsiConsole.MarkupLine($"[red][[ERROR]] An error ocurred while the installer tried to uninstall [red bold]{fancyPackageName}[/]. Please, run [red]{pipCommand}[/] manually to uninstall the conflicting package.[/]");
                    Environment.Exit(-1);
                }
                else
                {
                    AnsiConsole.MarkupLine($"[green][[INFO]] [red bold]{fancyPackageName}[/] was uninstalled successfully.[/]");
                }
            }
        }
    }
}
