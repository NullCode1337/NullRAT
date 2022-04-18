using System;
using System.Runtime.InteropServices;

namespace Nulllib;

internal static class Imported
{
    [DllImport("user32.dll")]
    internal static extern IntPtr GetSystemMenu(IntPtr windowHandler, bool bRevert);
    [DllImport("user32.dll")]
    internal static extern int DeleteMenu(IntPtr menuHandler, int nPosition, int wFlags);
    [DllImport("kernel32.dll", ExactSpelling = true)]
    internal static extern IntPtr GetConsoleWindow();
}
