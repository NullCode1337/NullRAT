namespace NullCode.Dependencies
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
				AnsiConsole.MarkupLine($"[green][[INFO]] {PackageName} is installed![/]");
				ProgramData.InstalledPackages++;
			}
			else
			{
				string pipCommand = "pip" + $" install {PackageName}";

				AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PackageName} not installed![/]");
				Thread.Sleep(2000);
				AnsiConsole.MarkupLine($"[orange1][[INFO]] Installing {PackageName}[/]");

				Thread VirtualEnvInstaller = new(
					() => cmdOutput = ProcessInvoker.RunCmd("pip", $"install {PackageName}", "y")
					);

				VirtualEnvInstaller.Start();


				while (VirtualEnvInstaller.IsAlive)
				{
					/*
					Thread.Sleep(500);
					Console.Write(".");
					*/
					Thread.Sleep(5);
				}

				if (cmdOutput.ExitCode != 0)
				{
					AnsiConsole.MarkupLine($"[maroon][[ERROR]] Error Installing {PackageName}. Pip exit code \"P{cmdOutput.ExitCode}\" does not indicate success!\nTry installing it with: [orange1]{pipCommand}[/][/]");
				}
                else
                {
					AnsiConsole.MarkupLine($"[green][[INFO]] {PackageName} has been successfully installed![/]");
					ProgramData.InstalledPackages++;
				}
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
			bool sourcePresent;

			if (ProgramData.PipPackageList.ToString().Contains(PipPackageName))
			{
				AnsiConsole.MarkupLine($"[green][[INFO]] {PipPackageName} is installed![/]");
				ProgramData.InstalledPackages++;
			}
			else
			{
				AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PipPackageName} not installed![/]");
				Thread.Sleep(2000);
				AnsiConsole.MarkupLine($"[orange1][[INFO]] Installing {PipPackageName}[/]");

				#region Download Source
				string PathToPackage = Environment.CurrentDirectory + @$"/{PipPackageName}-git.zip";
				PathToPackage = PathToPackage.Trim(Path.GetInvalidFileNameChars());

				HttpResponseMessage hrm0 = ProgramData.httpClient.GetAsync(GitPipPackage).GetAwaiter().GetResult();
                
				if (hrm0.IsSuccessStatusCode)
                {
					using (Stream stream = hrm0.Content.ReadAsStream())
					{
						using (FileStream fs = File.Create(PathToPackage))
						{
							stream.CopyTo(fs);
							sourcePresent = true;
						} 
					}
                } 
				else
                {
					Console.WriteLine($"[maroon][[ERROR]]Error Downloading source for {PipPackageName}![/]");
					sourcePresent = false;
                }
                #endregion

                string pipCommand = "pip" + $" install ";

				if (sourcePresent)
				{
					Thread VirtualEnvInstaller = new(
						() => cmdOutput = ProcessInvoker.RunCmd("pip", $"install {PathToPackage}", "y")
						);

					VirtualEnvInstaller.Start();

					while (VirtualEnvInstaller.IsAlive)
					{
						Thread.Sleep(5);
					}
				}
				if (cmdOutput.ExitCode != 0 || !sourcePresent)
				{
					AnsiConsole.MarkupLine($"[maroon][[ERROR]] Error Installing {PipPackageName}. Pip exit code \"P{cmdOutput.ExitCode}\" does not indicate success!\nTry obtaining the source and running: [orange1]{pipCommand}<PATH/TO/SOURCE>.zip[/][/]");
				}
				else
				{
					AnsiConsole.MarkupLine($"[green][[INFO]] {PipPackageName} has been successfully installed![/]");
					ProgramData.InstalledPackages++;
				}
			}
		}
	}
}
