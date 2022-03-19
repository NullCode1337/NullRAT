using System.Collections.Generic;
using System.Net;
using System.Net.Http;

namespace NullRAT.Dependencies
{
    public struct ProgramData
    {
        #region No Python Statements

        public const string noPython2 =
            "[maroon][[ERROR]] Python not found!" +
            "\n" +
            "-------------------------[/]";

        public const string noPython =
            "[red1]This is probably because Python is not installed," +
            "\r\n" +
            "or not added to PATH. If you are sure you have installed" +
            "\r\n" +
            "Python, please check if it is added to path properly." +
            "\r\n" +
            "\r\n" +
            "Otherwise, check your Python installation for errors.[/]";

        #endregion

        #region No Internet Statements

        public const string noInternet2 =
            "[maroon][[ERROR]] You don't have an internet connection!" +
            "\r\n" +
            "-----------------------------------------------[/]";

        public const string noInternet =
            "[red1]NullRAT Dependencies Installer requires an active" +
            "\r\n" +
            "internet connection to be able to install all the required dependencies." +
            "\r\n" +
            "\r\n" +
            "Please check your internet connection, and try again.[/]";

        #endregion
        public volatile static string[] PipPackageList;
        public volatile static int InstalledPackages;
        public volatile static int PackagesFailed;
        /// <summary>
        /// List of packages that failed to be installed.
        /// </summary>
        public static List<string> FailedPackages { get; set; } = new();
        /// <summary>
        /// List of packages to install
        /// </summary>
        /// <value>a String of the packages that require to be installed.</value>
        public static string[] Packages { get; } = new string[]
        {
            "virtualenv",
            "aiohttp",
            "disnake",
            "requests",
            "mss",
            "pyinstaller",
            "pyarmor"
        };
        // Avoid connection errors for problems with SSL or TLS by using TLS 1.2.
        private static readonly HttpClientHandler handler = new()
        {
            SslProtocols = System.Security.Authentication.SslProtocols.Tls12,
            UseCookies = false,
            AutomaticDecompression = DecompressionMethods.All,
        };
        public static HttpClient HttpClient { get; } = new(handler);
    }
}
