using System;
using System.Net;
using System.Threading;
using Spectre.Console;
using System.Threading.Tasks;
using static NullRAT.Dependencies.Text;
using System.Collections.Generic;
using System.Runtime.CompilerServices;

namespace NullRAT.Dependencies
{
// Converting null literal or possible null value to non-nullable type.
#pragma warning disable CS8600 
    public static class MainActivity
    {
        static async Task Main()
        {
            PackageManager pacman = new();
            // Disable changing console size and closing
            LockConsole.LockConsoleSizeXY();

            #region Presentation

            Console.Title = "NullRAT Dependencies Installer";
            Console.Clear();
            Console.WriteLine("");
            Utils.PrintNullRAT(); // Print NullRAT.

            AnsiConsole.Write(new Rule("[red]Dependencies Installer[/]").LeftAligned());
            AnsiConsole.WriteLine();

            #endregion

            #region Check Internet Connection

            IPAddress[] ipAddresses =
            {
                IPAddress.Parse("1.1.1.1"),
                IPAddress.Parse("1.0.0.1"),
                IPAddress.Parse("8.8.8.8"),
                IPAddress.Parse("8.8.4.4")
            };

            if (!CheckConnection.BatchPing(ipAddresses))
            {
                // Pings failed. Trying to send an HTTP request to https://www.google.com and https://www.github.com . If both fail. Exit.
                if (!await CheckConnection.SendPetition("https://www.google.com") && !await CheckConnection.SendPetition("https://www.github.com"))
                {
                    AnsiConsole.MarkupLine(ProgramData.noInternet2);
                    AnsiConsole.MarkupLine(ProgramData.noInternet);
                    Thread.Sleep(5000);
                    Environment.Exit(-1);
                }
            }

            #endregion

            #region Verify Environment.

            SlowPrint("Verifying Environment...", "aqua", true);
            AnsiConsole.Markup("[aqua]--------------------------\n[/]");

            await VerifyEnvironment.VerifyBasic(); // Verify basic environment.

            string[] IncompatiblePackages = new string[]
            {
                "discord.py",
                "py-cord",
                "enum34"
            }; // Breaking packages that cause conflict.

            SlowPrint("\nChecking for incompatible packages...", "aqua", true);
            AnsiConsole.Markup("[aqua]---------------------------------------\n[/]");

            bool incompatiblePgks = false;

            for (var i = 0; i < IncompatiblePackages.Length; i++)
            {
                for (int j = 0; j < ProgramData.PipPackageList.Length; j++)
                {
                    if (ProgramData.PipPackageList[j].Contains(IncompatiblePackages[i]))
                    {
                        incompatiblePgks = true;
                        AnsiConsole.MarkupLine($"[yellow][[WARN]] Detected [red]incompatible[/] package [red bold]{IncompatiblePackages[i]}[/]. Removing...[/]");
                        pacman.RemovePipPackage(IncompatiblePackages[i]);
                        AnsiConsole.MarkupLine($"[green][[INFO]] [red bold]{IncompatiblePackages[i]}[/] was removed successfully[/]");
                        break;
                    }
                }
            }

            if (!incompatiblePgks)
            {
                AnsiConsole.MarkupLine("[green][[INFO]] No [red bold]incompatible[/] packages detected![/]");
            }

            AnsiConsole.Status().Start("Updating PIP", ctx =>
            {
                ctx.Spinner(Spinner.Known.Ascii);
                ctx.SpinnerStyle = ctx.SpinnerStyle?.Decoration(Decoration.Bold);
                ProcessInvoker.RunCmd("python", "-m pip install --user --upgrade pip");
            });

            #endregion

            #region Install Dependencies

            SlowPrint("\nChecking PIP dependencies...", "aqua", true);
            AnsiConsole.MarkupLine("[aqua]------------------------------[/]");

            int pendingPkgCount = ProgramData.Packages.Length;

            List<Task> pipTasks = new();
            // For each package, run a thread to install it
            for (int i = 0; i < pendingPkgCount; i++)
            {
                pipTasks.Add(Task.Run(() => pacman.InstallPipPackage(ProgramData.Packages[i])));
                // Avoid some problems
                Thread.Sleep(50);
            }

            #endregion

            EndExecution(ref pipTasks);
        }
        static void EndExecution(ref List<Task> remainingTasks)
        {
            bool instFailed = false;
            while (remainingTasks.Count > 0)
            {
                Thread.Sleep(remainingTasks.Count * 10);
                Task finishedTask = Task.WhenAny(remainingTasks).Result;
                remainingTasks.Remove(finishedTask);
            }

            AnsiConsole.Write($"{Environment.NewLine}");
            AnsiConsole.Write(new Rule());

            if (ProgramData.PackagesFailed > 0)
            {
                for (int i = 0; i < ProgramData.FailedPackages.Count; i++)
                {
                    AnsiConsole.MarkupLine($"Run: [red]python -m pip install --no-input --user {ProgramData.FailedPackages[i]}[/] to install the package manually.");
                }
                instFailed = true;
            }
            if (!instFailed) {
                AnsiConsole.MarkupLine("\n[green][[INFO]] All packages have been installed successfully![/]\n");
            } else if (instFailed) {
                AnsiConsole.MarkupLine("\n[maroon][[WARN]] Unable to install some packages[/]");
                Environment.Exit(-1);
            }
            Environment.Exit(0);
        }
    }
}
