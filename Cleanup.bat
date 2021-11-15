@echo off & color 8F

attrib +h Cleanup.bat

mkdir "%~dp0\temp"
cd "%~dp0\src"

move RAT.py "%~dp0\"
move custom_icon.ico "%~dp0\"

cd "%~dp0\"
rmdir /s /q "%~dp0\src\"

mkdir "%~dp0\src\"
move RAT.py "%~dp0\src\"
move custom_icon.ico "%~dp0\src\"

move *.bat "%~dp0\temp"
if exist README.md (del README.md)
if exist .git\ (rmdir /s /q .git\)
move requirements.txt "%~dp0\temp"

del *.*
cd "%~dp0\temp"

move * "%~dp0\"
cd "%~dp0\"

rmdir /s /q "%~dp0\temp"
attrib -h Cleanup.bat