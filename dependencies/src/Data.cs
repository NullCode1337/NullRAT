namespace NullCode.Dependencies
{
    public class ProgramData
    {
        #region No Python Statements

        public static readonly string noPython2 = 
            "[maroon][[ERROR]] Python not found!" + 
            "\n" + 
            "-------------------------[/]";

        public static readonly string noPython = 
            "[red1]This is probably because Python is not installed," + 
            "\n" + 
            "or not added to PATH. If you are sure you have installed" + 
            "\n" + 
            "Python, please check if it is added to path properly." + 
            "\n" + 
            "\n" + 
            "Otherwise, check your Python installation for errors.[/]";

        #endregion

        #region No Internet Statements

        public static readonly string noInternet2 = 
            "[maroon][[ERROR]] You don't have an internet connection!" + 
            "\n" + 
            "-----------------------------------------------[/]";

        public static readonly string noInternet = 
            "[red1]NullRAT Dependencies Installer requires an active" + 
            "\n" + 
            "internet connection to be able to install all the required dependencies." +
            "\n" +
            "\n" +
            "Please check your internet connection, and try again.[/]";

        #endregion

        private static StringBuilder pipPackageList = new("");
        private static uint installedPackages = 1;
        private static uint packagesToInstall = 0;

        public static StringBuilder PipPackageList { get => pipPackageList; set => pipPackageList = value; }
        public static uint InstalledPackages { get => installedPackages; set => installedPackages = value; }
        public static uint PackagesToInstall { get => packagesToInstall; set => packagesToInstall = value; }
    }
}
