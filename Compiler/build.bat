@echo off
rem Put their respective bin folders in PATH
rem and %USERPROFILE%\.nimble\bin
rem https://nim-lang.org/download/nim-2.2.4_x64.zip
rem https://nim-lang.org/download/mingw64.7z

cd %~dp0
nimble install puppy
nim c -d:release -d:danger main.nim
move main.exe ..\Compiler.exe
cd %~dp0..