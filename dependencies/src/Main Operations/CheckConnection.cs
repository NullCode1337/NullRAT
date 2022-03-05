namespace NullRAT.Dependencies
{
    public static class CheckConnection
    {
        /// <summary>
        /// Send an ICMP echo message to the target IP.
        /// </summary>
        /// <param name="ObjectiveIP">Target IP Examples: 8.8.8.8, 8.8.4.4</param>
        /// <returns>true if the ping was a success, false if it was a failure</returns>
        public static bool Ping(IPAddress ObjectiveIP)
        {
            Ping ping = new();
            const string bufferText = "This is a ping";
            byte[] buffer = Encoding.UTF8.GetBytes(bufferText);

            PingReply reply = ping.Send(ObjectiveIP, 10, buffer);

            if (reply.Status == IPStatus.Success)
            {
                //There is an available Internet Connection -> PING was a success
                return true;
            }

            return false;
        }

        /// <summary>
        /// Sends an HTTP request
        /// </summary>
        /// <param name="URL">Website to ping</param>
        /// <returns>true if the HTTP code indicates success, false if it fails to perform the request, or it's code does not indicate success</returns>
        public static bool SendPetition(string URL)
        {
            return ProgramData.HttpClient.GetAsync(URL).GetAwaiter().GetResult().IsSuccessStatusCode;
        }
    }
}