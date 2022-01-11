namespace NullCode.Dependencies
{
	public struct CmdOutput
    {
		public StringBuilder Output = new();
		public int ExitCode = 0;
    }
    internal class ProcessInvoker
    {
		/// <summary>
		/// Runs an application inside of a Console and allows to input data
		/// </summary>
		/// <param name="ProgramPath">The Path to the .exe file, can be used with just filename if the application is on PATH.</param>
		/// <param name="Arguments">The arguments that the application has to run with</param>
		/// <param name="input">What to Input into the console</param>
		/// <returns>CmdOutput struct containing Output and the Console ExitCode</returns>
		public static CmdOutput RunCmd(string ProgramPath, string Arguments, string input)
		{
			CmdOutput output = new();
			Process process = new();
			
			//Process Vars
			process.StartInfo.FileName = ProgramPath;
			process.StartInfo.Arguments = Arguments;
			process.StartInfo.CreateNoWindow = true;
			process.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
			process.StartInfo.RedirectStandardOutput = true;
			process.StartInfo.RedirectStandardInput = true;

			process.Start();

			Thread.Sleep(1000);
			StreamWriter writer = process.StandardInput;
			writer.Write(input);
			
			process.WaitForExit();
			output.Output.Append(process.StandardOutput.ReadToEnd());
			output.ExitCode = process.ExitCode;

			return output;
		}
		/// <summary>
		/// Runs an application inside of a Console
		/// </summary>
		/// <param name="ProgramPath">The Path to the .exe file, can be used with just filename if the application is on PATH.</param>
		/// <param name="Arguments">The arguments that the application has to run with</param>
		/// <returns>CmdOutput struct containing Output and the Console ExitCode</returns>
		public static CmdOutput RunCmd(string ProgramPath, string Arguments)
		{
			CmdOutput output = new();
			Process process = new();

			//Process Arguments
			process.StartInfo.FileName = ProgramPath;
			process.StartInfo.Arguments = Arguments;
			process.StartInfo.CreateNoWindow = true;
			process.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
			process.StartInfo.RedirectStandardOutput = true;

			process.Start();

			process.WaitForExit();
			output.Output.Append(process.StandardOutput.ReadToEnd());
			output.ExitCode = process.ExitCode;

			return output;
		}
	}
}
