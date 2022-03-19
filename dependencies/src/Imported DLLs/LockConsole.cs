using Spectre.Console;
using System;

namespace NullRAT.Dependencies
{
    internal static class LockConsole
    {
        /// <summary>
        /// Locks the console X, Y size
        /// </summary>
        public static void LockConsoleSizeXY()
        {
            IntPtr handle = Imported.GetConsoleWindow();
            IntPtr sysMenu = Imported.GetSystemMenu(handle, false);

            if (handle != IntPtr.Zero)
            {
                int[] marshalResult = new int[4];
                marshalResult[0] = Imported.DeleteMenu(sysMenu, 0xF060, 0x00000000);
                marshalResult[1] = Imported.DeleteMenu(sysMenu, 0xF020, 0x00000000);
                marshalResult[2] = Imported.DeleteMenu(sysMenu, 0xF030, 0x00000000);
                marshalResult[3] = Imported.DeleteMenu(sysMenu, 0xF000, 0x00000000);

                for (var i = 0; i < marshalResult.Length; i++)
                {
                    if (marshalResult[i] is not 0x00000000) // If HRESULT of last W32 Marshal Operation is NOT success. Print.
                        AnsiConsole.MarkupLine($"Marshal Operation Error with W32 Code -> {marshalResult[i]}");
                }
            }
        }
    }
}
