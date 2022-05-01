@echo off & @title NullRAT Dependencies Installer & @color A


echo   _   _       _ _ _____         _______   _____                            _                 _           
echo  ^| ^\ ^| ^|     ^| ^| ^|  __ ^\     /^\^|__   __^| ^|  __ ^\                          ^| ^|               (_)          
echo  ^|  ^\^| ^|_   _^| ^| ^| ^|__) ^|   /  ^\  ^| ^|    ^| ^|  ^| ^| ___ _ __   ___ _ __   __^| ^| ___ _ __   ___ _  ___  ___ 
echo  ^| . ` ^| ^| ^| ^| ^| ^|  _  /   / /^\ ^\ ^| ^|    ^| ^|  ^| ^|/ _ ^\ '_ ^\ / _ ^\ '_ ^\ / _` ^|/ _ ^\ '_ ^\ / __^| ^|/ _ ^\/ __^|
echo  ^| ^|^\  ^| ^|_^| ^| ^| ^| ^| ^\ ^\  / ____ ^\^| ^|    ^| ^|__^| ^|  __/ ^|_) ^|  __/ ^| ^| ^| (_^| ^|  __/ ^| ^| ^| (__^| ^|  __/^\__ ^\
echo  ^|_^| ^\_^|^\__,_^|_^|_^|_^|  ^\_^\/_/    ^\_^\_^|    ^|_____/ ^\___^| .__/ ^\___^|_^| ^|_^|^\__,_^|^\___^|_^| ^|_^|^\___^|_^|^\___^|^|___/
echo                                                      ^| ^|                                                 
echo                                                      ^|_^|                                                 
echo.
echo Installing Dependencies...
echo --------------------------
echo.
python -m pip uninstall enum34
python -m pip install pyinstaller==4.10
python -m pip install --upgrade virtualenv aiohttp disnake requests mss pyarmor
