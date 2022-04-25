@echo off & @title NullRAT Compiler & @color A
mode con: cols=87 lines=30
setlocal EnableDelayedExpansion

:start
cls
echo    _   _       _ _ _____         _______    _____                      _ _           
echo   ^| ^\ ^| ^|     ^| ^| ^|  __ ^\     /^\^|__   __^|  / ____^|                    (_) ^|          
echo   ^|  ^\^| ^|_   _^| ^| ^| ^|__) ^|   /  ^\  ^| ^|    ^| ^|     ___  _ __ ___  _ __  _^| ^| ___ _ __ 
echo   ^| . ` ^| ^| ^| ^| ^| ^|  _  /   / /^\ ^\ ^| ^|    ^| ^|    / _ ^\^| '_ ` _ ^\^| '_ ^\^| ^| ^|/ _ ^\ '__^|
echo   ^| ^|^\  ^| ^|_^| ^| ^| ^| ^| ^\ ^\  / ____ ^\^| ^|    ^| ^|___^| (_) ^| ^| ^| ^| ^| ^| ^|_) ^| ^| ^|  __/ ^|   
echo   ^|_^| ^\_^|^\__,_^|_^|_^|_^|  ^\_^\/_/    ^\_^\_^|     ^\_____^\___/^|_^| ^|_^| ^|_^| .__/^|_^|_^|^\___^|_^|   
echo                                                                 ^| ^|                  
echo                                                                 ^|_^|                  
echo.
echo ^>^> Options:
echo -----------
echo.

choice /c YN /n /m "Do you want to obfuscate the executable? [Y/N]: "
if %errorlevel%==1 (set pyarmor=yes) else (set pyarmor=no)

choice /c YN /n /m "Do you want to compress the executable? [Y/N]: "
if %errorlevel%==1 (set upxdd=yes) else (set upxdd=no)

choice /c YN /n /m "Do you want to add a custom icon? [Y/N]: "
if %errorlevel%==1 (set icon=yes) else (set icon=no)

echo. & echo All options selected: & echo ------------------------------------------
echo Obfuscating the executable=%pyarmor%
echo Compressing the executable=%upxdd%
echo Adding a custom icon to the executable=%icon%
echo ------------------------------------------

echo. & choice /c YN /n /m "Are all these options correct? [Y/N]: "
if %errorlevel%==2 (goto start) else (goto compile)

:compile
mode con: cols=87 lines=40
cls
echo ====================================================================================

echo    _   _       _ _ _____         _______    _____                      _ _           
echo   ^| ^\ ^| ^|     ^| ^| ^|  __ ^\     /^\^|__   __^|  / ____^|                    (_) ^|          
echo   ^|  ^\^| ^|_   _^| ^| ^| ^|__) ^|   /  ^\  ^| ^|    ^| ^|     ___  _ __ ___  _ __  _^| ^| ___ _ __ 
echo   ^| . ` ^| ^| ^| ^| ^| ^|  _  /   / /^\ ^\ ^| ^|    ^| ^|    / _ ^\^| '_ ` _ ^\^| '_ ^\^| ^| ^|/ _ ^\ '__^|
echo   ^| ^|^\  ^| ^|_^| ^| ^| ^| ^| ^\ ^\  / ____ ^\^| ^|    ^| ^|___^| (_) ^| ^| ^| ^| ^| ^| ^|_) ^| ^| ^|  __/ ^|   
echo   ^|_^| ^\_^|^\__,_^|_^|_^|_^|  ^\_^\/_/    ^\_^\_^|     ^\_____^\___/^|_^| ^|_^| ^|_^| .__/^|_^|_^|^\___^|_^|   
echo                                                                 ^| ^|                  
echo                                                                 ^|_^|                  

echo ==================================================================================== & echo.

cd "%~dp0NullRAT\"
if %icon%==yes (
	set /P "iconP=Please type the path of the custom icon: " 
	move "!iconP!" "%~dp0NullRAT\custom_icon.ico"
)
if %upxdd%==yes (set path=%path%;%~dp0NullRAT\upx)

if %pyarmor%==yes (
	if %icon%==yes (
		pyarmor pack -e " --onefile --noconsole --icon=custom_icon.ico " RAT.py
	) else (
		pyarmor pack -e " --onefile --noconsole " RAT.py
	)
) else (
	if %icon%==yes (
		pyinstaller --onefile --noconsole --icon=custom_icon.ico RAT.py
	) else (
		pyinstaller --onefile --noconsole RAT.py
	)
)

move dist\RAT.exe "%~dp0" & echo.
timeout /t 5 & EXIT
