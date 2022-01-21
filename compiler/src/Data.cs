namespace NullRAT.Compiler
{
    public struct RequestResponse
    {
        public HttpStatusCode StatusCode { get; set; }
        public StringBuilder DataAsString { get; set; } = new();
        public Stream DataAsStream { get; set; }
    }
    public struct WebData
    {
        private static CookieContainer CookieContainer = new();
        private static readonly HttpClientHandler Handler = new()
        {
            SslProtocols = System.Security.Authentication.SslProtocols.Tls12,
            UseCookies = true,
            CookieContainer = CookieContainer,
            AutomaticDecompression = DecompressionMethods.All
        };
        /// <summary>
        /// The program's main and only HttpClient.
        /// </summary>
        public static HttpClient HttpClient { get; } = new(Handler);
    }
    public struct InstanceData
    {
        public static bool UpdateAvailable = false;
        public static bool MakeWithCIcon = false;
        public static bool UseUPX = false;
    }
    public struct RATVariables
    {
        public StringBuilder Bot_Token { get; set; } = new();
        public ulong Notification_Channel_ID { get; set; } = new();
        public List<ulong> Server_IDs { get; set; } = new();
    }
}