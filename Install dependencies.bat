@echo off & color 8F

cd "%~dp0\src"
pip install -r requirements.txt
cls & echo Everything should be installed
pause >nul & exit /b 0
