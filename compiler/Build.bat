@echo off

:: Publish NullRAT Compiler 
:: for Windows x86 | Self Contained & Trimmed
dotnet publish "NullRAT Compiler.csproj" --output build\ --framework net6.0 --arch x86 --os win -c release --self-contained true