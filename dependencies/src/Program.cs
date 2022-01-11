using static NullCode.Dependencies.Text;

namespace NullCode.Dependencies
{
    #pragma warning disable CS8600 // Converting null literal or possible null value to non-nullable type.
    class Program
    {
		static void Main()
        {
            //Lock cmd
            LockConsole.LockConsoleSizeXY();

            #region Presentation

            Console.Title = "NullRAT Dependencies Installer";
			Console.Clear(); 
			Console.WriteLine("");
			CenterText(" ███▄    █  █    ██  ██▓     ██▓     ██▀███   ▄▄▄     ▄▄▄█████▓", "#6A66FF");
			CenterText(" ██ ▀█   █  ██  ▓██▒▓██▒    ▓██▒    ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒", "#6A66FF");
			CenterText("▓██  ▀█ ██▒▓██  ▒██░▒██░    ▒██░    ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░", "#6A66FF");
			CenterText("▓██▒  ▐▌██▒▓▓█  ░██░▒██░    ▒██░    ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ", "#6A66FF");
			CenterText("▒██░   ▓██░▒▒█████▓ ░██████▒░██████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ", "#6A66FF");
			CenterText("░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▓  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ", "#6A66FF");
			CenterText("░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░ ▒  ░░ ░ ▒  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░    ", "#6A66FF");
			CenterText("   ░   ░ ░  ░░░ ░ ░   ░ ░     ░ ░     ░░   ░   ░   ▒    ░      ", "#6A66FF");

			AnsiConsole.Write(new Rule("[red]Dependencies Installer[/]").LeftAligned());
            AnsiConsole.WriteLine();
            
			#endregion

            #region Check Internet Connection
            string[] ipAddresses = { "1.1.1.1", "1.0.0.1", "8.8.8.8", "8.8.4.4" };
            bool[] result = new bool[4];

            //Iterate through the ipAddresses array
            for (int i = 0; i < ipAddresses.Length; i++)
            {
                try
                {
                    if (IPAddress.TryParse(ipAddresses[i], out IPAddress ip))
                    {
                        if (!CheckConnection.Ping(ip))
                        {
                            result[i] = false;
                        }
                        else
                        {
                            result[i] = true;
                            break;
                        }
                    }
                    else
                    {
                        throw new Exception("IP Address couldn't be parsed.");
                    }
                }
                catch
                {
                    AnsiConsole.MarkupLine("The IP Couldn't be parsed...");
                }
            }

            if (!result.Contains(true))
			{
				//Pings Failed. Trying to send an HTTP request to https://www.google.com with TLS 1.2. If it fails, then send a request to https://www.github.com with TLS 1.2
				if (CheckConnection.SendPetition("https://www.google.com", System.Security.Authentication.SslProtocols.Tls12))
				{
					//Pings seem to be disabled  ¯\_(ツ)_/¯
				}
				else if (CheckConnection.SendPetition("https://www.github.com", System.Security.Authentication.SslProtocols.Tls12))
				{
					//Pings seem to be disabled  ¯\_(ツ)_/¯
				} 
				else
                {
					AnsiConsole.MarkupLine(ProgramData.noInternet2);
					AnsiConsole.MarkupLine(ProgramData.noInternet);
					System.Threading.Thread.Sleep(5000);
					Environment.Exit(2);
				}
			}
            #endregion

            #region Verify Environment and Install Packages!
            SlowPrint("Verifying Environment...\n", "aqua");
			AnsiConsole.Markup("[aqua]--------------------------\n[/]");

			VerifyEnvironment.VerifyPipAndPython();

			SlowPrint("\nChecking PIP dependencies...\n", "aqua");
			AnsiConsole.MarkupLine("[aqua]------------------------------\n[/]");

            //Add the package names.
			string[] packages = 
            {
                "virtualenv",
                "aiohttp", 
                "git+git://github.com/Pycord-Development/pycord@master",
                "requests", 
                "mss", 
                "pyinstaller",
		"pyarmor"
            };

            //All Packages "FancyNames"
            string[] fancyNames =
            {
                "Virualenv",
                "aioHTTP",
                "Pycord",
                "Requests",
                "MSS",
                "PyInstaller",
		"PyArmor"
            };

            ProgramData.PackagesToInstall = (uint)packages.Length;

            // For each Package, run a thread installing it
            
            for (int i = 0; i < packages.Length; i++)
            {
                Thread PipInstall;

                if (!packages[i].Contains("git+git"))
                {
                     PipInstall = new(() => InstallPackage.InstallPipPackage(packages[i]));
                } 
                else
                {
                    PipInstall = new(() => InstallPackage.InstallPipPackage(fancyNames[i], packages[i]));
                
                }
                PipInstall.Name = $"- Pip Instance {i}";
                PipInstall.IsBackground = true;
                PipInstall.Start();
                //Avoid nasty bugs
                Thread.Sleep(500);
            }

#endregion
            
            Thread exitThread = new(() => Exit.ExitProgram());
            exitThread.Start();

        }
	}
}
