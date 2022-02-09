namespace NullRAT.Dependencies
{
    public struct PingInformation
    {
        public Ping ping = new();
        public PingReply? reply;
    }
    internal class CheckConnection
    {
        /// <summary>
        /// Send an ICMP echo message to the target IP.
        /// </summary>
        /// <param name="ObjectiveIP">Target IP Examples: 8.8.8.8, 8.8.4.4</param>
        /// <returns>true if the ping was a sucess, false if it was a failure</returns>
        public static bool Ping(IPAddress ObjectiveIP)
        {
            PingInformation pingInf = new();
            string bufferText = "This is a Ping";
            byte[] buffer = Encoding.UTF8.GetBytes(bufferText);

            pingInf.reply = pingInf.ping.Send(ObjectiveIP, 10, buffer);

            if(pingInf.reply.Status == IPStatus.Success)
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
        /// <returns>true if the HTTP code indicates sucess, false if it fails to perform the request, or it's code does not indicate success</returns>
        public static bool SendPetition(string URL)
        {
            try
            {

                HttpResponseMessage _hrm = ProgramData.HttpClient.GetAsync(URL).GetAwaiter().GetResult();
                _hrm.EnsureSuccessStatusCode();
                return true;
            }
            catch
            {
                //Error effectuating the GET Request to the URL
                return false;
            }
        }
    }
}
