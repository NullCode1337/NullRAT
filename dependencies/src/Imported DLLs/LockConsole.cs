namespace NullCode.Dependencies
{
    internal class LockConsole
    {
        /// <summary>
        /// Locks the console X, Y size
        /// </summary>
        public static void LockConsoleSizeXY()
        {
            IntPtr handle = GetConsoleWindow();
            IntPtr sysMenu = GetSystemMenu(handle, false);

            if (handle != IntPtr.Zero)
            {
                try
                {
                    //Discard return(Int32)
                    _ = DeleteMenu(sysMenu, 0xF060, 0x00000000);
                    _ = DeleteMenu(sysMenu, 0xF020, 0x00000000);
                    _ = DeleteMenu(sysMenu, 0xF030, 0x00000000);
                    _ = DeleteMenu(sysMenu, 0xF000, 0x00000000);
                }
                catch
                {

                }
            }
        }

        [DllImport("user32.dll")]
        private static extern IntPtr GetSystemMenu(IntPtr hWnd, bool bRevert);

        [DllImport("user32.dll")]
        public static extern int DeleteMenu(IntPtr hMenu, int nPosition, int wFlags);

        [DllImport("kernel32.dll", ExactSpelling = true)]
        private static extern IntPtr GetConsoleWindow();
    }
}
