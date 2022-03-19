using System.Diagnostics;
using System.Threading.Tasks;
using System.Text;
using System.Threading;
using System;

namespace NullRAT.Dependencies
{
    public struct CmdOutput
    {
        public StringBuilder Output;
        public StringBuilder ErrorO;
        public int ExitCode;
    }

    public static class ProcessInvoker
    {
        /// <summary>
        /// Runs an application inside of a Console
        /// </summary>
        /// <param name="ProgramPath">The Path to the .exe file, can be used with just filename if the application is on PATH.</param>
        /// <param name="Arguments">The arguments that the application has to run with</param>
        /// <returns>CmdOutput struct containing Output and the Console ExitCode</returns>
        public static CmdOutput RunCmd(string ProgramPath, string Arguments)
        {
            Process process = new();

            //Process Arguments
            process.StartInfo.FileName = ProgramPath;
            process.StartInfo.Arguments = Arguments;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            process.StartInfo.RedirectStandardError = true;
            process.StartInfo.RedirectStandardOutput = true;

            if(!process.Start())
            {
                throw new InvalidOperationException("Could not start the application with the specified parameters.");
            }
            process.WaitForExit();

            return new()
            {
                Output = new(process.StandardOutput.ReadToEnd()),
                ErrorO = new(process.StandardError.ReadToEnd()),
                ExitCode = process.ExitCode
            };
        }
    }
}