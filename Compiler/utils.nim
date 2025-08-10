import std/terminal
import std/os
import std/strformat

proc printName*() = 
    discard execShellCmd("cls")
    echo ""
    stdout.styledWriteLine(fgRed, "  ███╗   ██╗██╗   ██╗██╗     ██╗     ██████╗  █████╗ ████████╗")
    stdout.styledWriteLine(fgRed, "  ████╗  ██║██║   ██║██║     ██║     ██╔══██╗██╔══██╗╚══██╔══╝")
    stdout.styledWriteLine(fgRed, "  ██╔██╗ ██║██║   ██║██║     ██║     ██████╔╝███████║   ██║")
    stdout.styledWriteLine(fgRed, "  ██║╚██╗██║██║   ██║██║     ██║     ██╔══██╗██╔══██║   ██║")
    stdout.styledWriteLine(fgRed, "  ██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║██║  ██║   ██║")
    stdout.styledWriteLine(fgRed, "  ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝")
    stdout.styledWriteLine(fgRed, "  =========================================================")
    echo ""

proc cleanWorkingDir*() =
    echo ""
    var appDirectory = getAppDir()
    setCurrentDir(appDirectory)
    echo getCurrentDir()

    if dirExists(absolutePath("NullRAT")):
        createDir("NullRAT2")

        moveFile(absolutePath("NullRAT" / "custom_icon.ico"), appDirectory / "NullRAT2" / "custom_icon.ico")
        moveFile(absolutePath("NullRAT" / "RAT.py"), appDirectory / "NullRAT2" / "RAT.py")
        moveDir(absolutePath("NullRAT" / "modules"), appDirectory / "NullRAT2" / "modules")
        moveDir(absolutePath("NullRAT" / "upx"), appDirectory / "NullRAT2" / "upx")

        # check existing variables
        if fileExists(absolutePath("NullRAT" / "Variables.py")):
            var inp: char
            echo "Existing Variables file found! Preserve? (y/N)"
            inp = getch()
            if inp == 'Y' or inp == 'y':
                moveFile(absolutePath("NullRAT" / "Variables.py"), appDirectory / "NullRAT2" / "Variables.py")

        removeDir("NullRAT")
        moveDir(appDirectory / "NullRAT2", appDirectory / "NullRAT")
        
    # remove git stuff if downloaded from source
    if dirExists(absolutePath(".git")):
        echo "Remove git files? (y/N)"
        var inpu: char = getch()
        if inpu == 'y' or inpu == 'Y':
            removeDir(".git")
            removeDir("Compiler")
            removeFile("README.md")
            removeFile("Getting Variables.md")
            removeFile(".gitignore")

    removeDir("build")
    removeDir("dist")

proc runInVenv*(venvPath: string, command: string): int =
    return execShellCmd(fmt"""{venvPath}\Scripts\{command}""")