@echo off & @title NullRAT Dependencies Installer & @color A

echo Installing Dependencies...
echo --------------------------
echo.
python -m pip install virtualenv aiohttp disnake requests mss pyinstaller pyarmor
