using System.Net;
using System.Net.NetworkInformation;
using System.Net.Http;
using System.Threading.Tasks;
using System.Text;

namespace NullRAT.Dependencies;
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
        const string bufferText = "YOOO, Wacha doing server?";
        byte[] buffer = Encoding.UTF8.GetBytes(bufferText);

        PingReply reply = ping.Send(ObjectiveIP, 10, buffer);

        if (reply.Status is IPStatus.Success)
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
    public static async Task<bool> SendPetition(string URL)
    {
        HttpRequestMessage request = new()
        {
            RequestUri = new(URL),
            Method = HttpMethod.Head
        };
        return (await ProgramData.HttpClient.SendAsync(request)).IsSuccessStatusCode;
    }
    /// <summary>
    ///  Pings the specified IPAddresses.
    /// </summary>
    /// <param name="targets">Target Addresses</param>
    /// <returns>returns true if ANY of the addreses response with <seealso name="IPStatus.Success"/>, else false</returns>
    public static bool BatchPing(IPAddress[] targets)
    {
        for (int i = 0; i < targets.Length; i++)
        {
            if (Ping(targets[i])) return true; // If any of the pings are true, return true. Otherwise, return false.
        }
        return false;
    }
}