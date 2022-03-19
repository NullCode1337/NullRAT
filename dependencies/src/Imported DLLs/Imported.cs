using System;
using System.Runtime.InteropServices;

namespace NullRAT.Dependencies;

internal static class Imported
{
        [DllImport("user32.dll")]
        public static extern IntPtr GetSystemMenu(IntPtr windowHandler, bool bRevert);
        [DllImport("user32.dll")]
        public static extern int DeleteMenu(IntPtr menuHandler, int nPosition, int wFlags);
        [DllImport("kernel32.dll", ExactSpelling = true)]
        public static extern IntPtr GetConsoleWindow();
}
