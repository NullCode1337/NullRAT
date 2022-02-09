namespace NullRAT.Dependencies
{
    public struct ProgramData
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
        private static uint installedPackages = 0;
        private static uint packagesToInstall = 0;
        private static uint packagesFailed = 0;
        private static string[]? fancyNames;
        private static string[]? packages;

        public static StringBuilder PipPackageList { get => pipPackageList; set => pipPackageList = value; }
        public static uint InstalledPackages { get => installedPackages; set => installedPackages = value; }
        public static uint PackagesToInstall { get => packagesToInstall; set => packagesToInstall = value; }
        public static uint PackagesFailed { get => packagesFailed; set => packagesFailed = value; }
        public static List<string> FailedPackages { get; set; } = new();
        public static string[]? FancyNames { get => fancyNames; set => fancyNames = value; }
        public static string[]? Packages { get => packages; set => packages = value; }

        // Avoid connection errors for problems with SSL or TLS by using TLS 1.2.
        // Use Cookies & Container + Decompression.

        //Web Stuff
        private static readonly CookieContainer cookies = new();

        private static readonly HttpClientHandler handler = new()
        {
            SslProtocols = System.Security.Authentication.SslProtocols.Tls12,
            UseCookies = true,
            AutomaticDecompression = DecompressionMethods.All,
            CookieContainer = cookies
        };

        private static readonly HttpClient internalHttpClient = new(handler);
        public static HttpClient HttpClient { get => internalHttpClient; set => value = internalHttpClient; }

    }
}
