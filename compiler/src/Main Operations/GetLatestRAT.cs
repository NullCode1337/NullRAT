namespace NullRAT.Compiler.Updater
{
    public class GetLatestRAT
    {
        public static bool CalculateSHA256(Stream File0, string PathToFile1)
        {
            SHA256 SHA2560 = SHA256.Create();
            try
            {
                //Calculate hash of original RAT.py
                using FileStream fs = File.OpenRead(PathToFile1);
                byte[] objectiveHash0 = SHA2560.ComputeHash(fs);
                string stringObjHash0 = BitConverter.ToString(objectiveHash0).Replace("-", String.Empty);

                //Calculate hash of new RAT.py
                byte[] objectiveHash1 = SHA2560.ComputeHash(File0);
                string stringObjHash1 = BitConverter.ToString(objectiveHash1).Replace("-", String.Empty);

                if (stringObjHash0 == stringObjHash1)
                {
                    return true;
                }
            }
            catch (Exception ex)
            {
            }
            return false;

        }
        public static RequestResponse GetRAT(string DownloadURL, HttpClient client)
        {
            RequestResponse response = new();
            HttpResponseMessage hrm = client.GetAsync(DownloadURL).GetAwaiter().GetResult();

            response.StatusCode = hrm.StatusCode;
            if (hrm.IsSuccessStatusCode)
            {
                response.DataAsStream = hrm.Content.ReadAsStream();
                response.DataAsString.Append(hrm.Content.ReadAsStringAsync().GetAwaiter().GetResult());
            }
            return response;
        }
    }
}
