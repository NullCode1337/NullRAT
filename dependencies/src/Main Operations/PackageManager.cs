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
            CmdOutput cmdOutput = new();

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
                    () => cmdOutput = ProcessInvoker.RunCmd("python", $"-m pip install {PackageName} --user", "y")
                    );

                VirtualEnvInstaller.Start();


                while (VirtualEnvInstaller.IsAlive)
                {
                    Thread.Sleep(5);
                }

                if (cmdOutput.ExitCode != 0 && cmdOutput.ExitCode != 1)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] Error Installing {PackageName}. Pip exit code \"{cmdOutput.ExitCode}\" does not indicate success!\nTry installing it with: [orange1]{pipCommand}[/][/]");
                    ProgramData.PackagesFailed++;
                    AnsiConsole.MarkupLine($"--------PIP OUTPUT\n{cmdOutput.Output.ToString().RemoveMarkup()}\n--------END OUTPUT");
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
        /// <param name="PipPackageName">The name of the package on Pip Freeze</param>
        /// <param name="GitPipPackage">Link to github Repository source, must be in zip!</param>
        /// <exception cref="Exception">Thrown when the package couldn't be installed successfully</exception>
        public static void InstallPipPackage(string PipPackageName, string GitPipPackage)
        {
            CmdOutput cmdOutput = new();
            string PathToPackage = Path.GetTempFileName(),
                   FinalPath = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData) + @$"/pip/local-paclages0/";

            bool sourcePresent = false;

            if (ProgramData.PipPackageList.ToString().Contains(PipPackageName))
            {
                Text.SlowPrintI($"{PipPackageName} is installed!", "green", true);
                ProgramData.InstalledPackages++;
            }
            else
            {
                Thread.Sleep(1000);
                lock (Text.slowPrintLock)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PipPackageName} not installed![/]");
                }
                Thread.Sleep(1000);
                Text.SlowPrintI($"Installing {PipPackageName}...", "orange1", true);

                #region Download Source
                try
                {

                    PathToPackage = PathToPackage.Trim(Path.GetInvalidFileNameChars());

                    HttpResponseMessage hrm0 = ProgramData.HttpClient.GetAsync(GitPipPackage).GetAwaiter().GetResult();

                    if (hrm0.IsSuccessStatusCode)
                    {
                        using (Stream stream = hrm0.Content.ReadAsStream())
                        {
                            using (FileStream fs = File.Create(PathToPackage))
                            {

                                stream.CopyTo(fs);
                                sourcePresent = true;
                                fs.Dispose();
                                fs.Close();
                            }
                            stream.Dispose();
                            stream.Close();
                        }
                        Directory.CreateDirectory(FinalPath);
                        FinalPath += $"{PipPackageName}-git@master.zip";
                        File.Move(PathToPackage, FinalPath, true);
                    }
                    else
                    {
                        AnsiConsole.MarkupLine($"[maroon][[ERROR]] Error Downloading source for {PipPackageName}![/]");
                        sourcePresent = false;
                    }
                }
                catch (Exception ex)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] An error occurred while we tried to download a package! {ex.Message}[/]");
                    sourcePresent = false;
                }
                #endregion

                string pipCommand = "pip" + $" install ";

                if (sourcePresent)
                {
                    Thread VirtualEnvInstaller = new(
                        () => cmdOutput = ProcessInvoker.RunCmd("python", $"-m pip install \"{FinalPath}\" --user")
                        );

                    VirtualEnvInstaller.Start();

                    while (VirtualEnvInstaller.IsAlive)
                    {
                        Thread.Sleep(5);
                    }
                }
                if (!sourcePresent || cmdOutput.ExitCode != 0)
                {
                    AnsiConsole.MarkupLine($"[maroon][[ERROR]] Error Installing {PipPackageName}. Pip exit code \"{cmdOutput.ExitCode}\" does not indicate success!\nTry running: [orange1]{pipCommand}{GitPipPackage}[/][/]");
                    ProgramData.PackagesFailed++;
                    AnsiConsole.MarkupLine($"--------PIP OUTPUT\n{cmdOutput.ErrorO.ToString().RemoveMarkup()}\n--------END OUTPUT");
                }
                else
                {
                    Text.SlowPrintI($"{PipPackageName} has been successfully installed!", "green", true);
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
