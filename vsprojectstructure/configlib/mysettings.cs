using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

namespace configlib
{
    public class MySettings
    {
        public void ReadSettings()
        {
            try
            {
                var config = ConfigurationManager.OpenMappedExeConfiguration(
                    new ExeConfigurationFileMap() { ExeConfigFilename = "configlib.dll.config" },
                    ConfigurationUserLevel.None);

                Console.WriteLine("in this case i am reading the settings from configlib's .config file");
                var appSettings = config.AppSettings.Settings;
                if (appSettings.Count == 0)
                {
                    Console.WriteLine("AppSettings is empty.");
                }
                else
                {
                    foreach (var key in appSettings.AllKeys)
                    {
                        Console.WriteLine("Key: {0} Value: {1}", key, appSettings[key].Value);
                    }
                }

                Console.WriteLine("this would read the settings from the current exes .config file");
                var appSettings2 = ConfigurationManager.AppSettings;
                if (appSettings2.Count == 0)
                {
                    Console.WriteLine("AppSettings is empty.");
                }
                else
                {
                    foreach (var key in appSettings2.AllKeys)
                    {
                        Console.WriteLine("Key: {0} Value: {1}", key, appSettings2[key]);
                    }
                }

            }
            catch (ConfigurationErrorsException)
            {
                Console.WriteLine("Error reading app settings");
            }
        }
    }
}
