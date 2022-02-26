using static NullRAT.Dependencies.Text;

namespace NullRAT.Dependencies
{
// Converting null literal or possible null value to non-nullable type.
#pragma warning disable CS8600 
    class Program
    {
        static void Main()
        {
            // Disable changing console size and closing
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
                        throw new Exception("Unable to parse IP Address");
                    }
                }
                catch
                {
                    AnsiConsole.MarkupLine("The IP Address couldn't be parsed");
                }
            }

            if (!result.Contains(true))
            {
                // Pings failed. Trying to send an HTTP request to https://www.google.com. If it fails, then send a request to https://www.github.com
                if (CheckConnection.SendPetition("https://www.google.com"))
                {
                    // Pinging seems to be disabled. Nothing to do
                }
                else if (CheckConnection.SendPetition("https://www.github.com"))
                {
                    // Pinging seems to be disabled. Nothing to do
                }
                else
                {
                    AnsiConsole.MarkupLine(ProgramData.noInternet2);
                    AnsiConsole.MarkupLine(ProgramData.noInternet);
                    System.Threading.Thread.Sleep(5000);
                    Environment.Exit(-1);
                }
            }
            #endregion

            #region Verify Environment and Install Packages!
            SlowPrint("Verifying Environment...", "aqua", true);
            AnsiConsole.Markup("[aqua]--------------------------\n[/]");

            VerifyEnvironment.VerifyPipAndPython();

            string[] IncompatiblePackages = new string[2]
            {
                "discord.py", "py-cord" // Breaking packages that shouldn't exist
            };
            SlowPrint("\nUninstalling incompatible packages...", "aqua", true);
            AnsiConsole.Markup("[aqua]---------------------------------------\n[/]");

            string[] installedpkg = ProgramData.PipPackageList.ToString().Split('\n');
            bool noIncompatibilities = true;

            for (var i = 0; i < IncompatiblePackages.Length; i++)
            {
                //Make a new Thread that searches for the packages that are not compatible.
                new Thread(() =>
                {
                    int i0 = i;
                    for (int i1 = 0; i1 < installedpkg.Length; i1++)
                    {
                        if (installedpkg[i1].Contains(IncompatiblePackages[i]))
                        {
                            noIncompatibilities = false;
                            AnsiConsole.MarkupLine($"[yellow][[WARN]] Detected [red]incompatible[/] package [red bold]{IncompatiblePackages[i]}[/]. Uninstalling...[/]");
                            RemovePackage.RemovePipPackage(IncompatiblePackages[i]);
                        }
                    }
                }).Start();
                
                Thread.Sleep(500);
            }
            Thread.Sleep(1500);
            if (noIncompatibilities)
            {
                AnsiConsole.MarkupLine($"[green][[INFO]] No [red bold]incompatible[/] packages detected![/]");
            }

            AnsiConsole.Status().StartAsync("Updating PIP", ctx =>
            {
                ctx.Spinner(Spinner.Known.Ascii);
                ctx.SpinnerStyle.Decoration(Decoration.Bold);
                ProcessInvoker.RunCmd("python", "-m pip install --user --upgrade pip");
                return Task.CompletedTask;
            });


            SlowPrint("\nChecking PIP dependencies...", "aqua", true);
            AnsiConsole.MarkupLine("[aqua]------------------------------[/]");

            //Add the package names.
            ProgramData.Packages = new string[]
            {
                "virtualenv",
                "aiohttp",
                "disnake",
                "requests",
                "mss",
                "pyinstaller",
                "pyarmor"
            };

            //All Packages "FancyNames" to search on pip freeze, only 'special' cases
            ProgramData.FancyNames = new string[]
            {
                "virtualenv",
                "aiohttp",
                "disnake",
                "requests",
                "mss",
                "pyinstaller",
                "pyarmor"
            };

            ProgramData.PackagesToInstall = (uint)ProgramData.Packages.Length;

            // For each package, run a thread to install it
            for (int i = 0; i < ProgramData.Packages.Length; i++)
            {
                Thread PipInstall;

                if (!ProgramData.Packages[i].Contains("github"))
                {
                    PipInstall = new(() => InstallPackage.InstallPipPackage(ProgramData.Packages[i]));
                }
                else
                {
                    PipInstall = new(() => InstallPackage.InstallPipPackage(ProgramData.FancyNames[i], ProgramData.Packages[i]));
                }
                PipInstall.Name = $"- Pip Instance {i}";
                PipInstall.IsBackground = true;
                PipInstall.Start();
                //Avoid nasty bugs
                Thread.Sleep(50);
            }

            #endregion

            Thread exitThread = new(() => Exit.ExitProgram());
            exitThread.Start();

        }
    }
}
