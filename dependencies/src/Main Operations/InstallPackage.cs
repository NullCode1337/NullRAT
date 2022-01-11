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
				AnsiConsole.MarkupLine($"[green][[INFO]] {PackageName} installed![/]");
				ProgramData.InstalledPackages++;
			}
			else
			{
				string pipCommand = "pip" + $"install {PackageName}";

				AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PackageName} not installed![/]");
				Thread.Sleep(3000);
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
					AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PackageName} couldn't be installed![/]");
					throw new Exception($"Failed to install pip package: {PackageName} | Try installing it yourself with the command: {pipCommand}");
				}
                else
                {
					AnsiConsole.MarkupLine($"[green][[INFO]] {PackageName} successfully installed![/]");
					ProgramData.InstalledPackages++;
				}
			}
		}
		/// <summary>
		/// Install a PIP Package that comes from Git and requires "special" treatment
		/// </summary>
		/// <param name="PipPackageName">The name of the package on Pip Freeze</param>
		/// <param name="GitPipPackage">Link to github Repository</param>
		/// <exception cref="Exception">Thrown when the package couldn't be installed successfully</exception>
		public static void InstallPipPackage(string PipPackageName, string GitPipPackage)
		{
			CmdOutput cmdOutput = new();

			if (ProgramData.PipPackageList.ToString().Contains(PipPackageName))
			{
				AnsiConsole.MarkupLine($"[green][[INFO]] {PipPackageName} installed![/]");
			}
			else
			{
				string pipCommand = "pip" + $"install {GitPipPackage}";

				AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PipPackageName} not installed![/]");
				Thread.Sleep(3000);
				AnsiConsole.MarkupLine($"[orange1][[INFO]] Installing {PipPackageName}[/]");

				Thread VirtualEnvInstaller = new(
					() => cmdOutput = ProcessInvoker.RunCmd("pip", $"install {GitPipPackage}", "y")
					);

				VirtualEnvInstaller.Start();


				while (VirtualEnvInstaller.IsAlive)
				{
					Thread.Sleep(5);
				}

				if (cmdOutput.ExitCode != 0)
				{
					AnsiConsole.MarkupLine($"[maroon][[ERROR]] {PipPackageName} couldn't be installed![/]");
					throw new Exception($"Failed to install pip package: {PipPackageName} | Try installing it yourself with the command: {pipCommand}");
				}
				else
				{
					AnsiConsole.MarkupLine($"[green][[INFO]] {PipPackageName} successfully installed![/]");
					ProgramData.InstalledPackages++;
				}
			}
		}
	}
}
