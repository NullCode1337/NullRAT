@echo off

cd %~dp0
nimble install puppy
nim c -d:release -d:danger main.nim
move main.exe ..\compiler.exe
cd %~dp0..