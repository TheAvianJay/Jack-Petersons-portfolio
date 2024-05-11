using System;
using System.Net;
using System.Net.Http;
using System.Text.Json;

class Program
{
    static async Task Main(string[] args)
    {
        using var client = new HttpClient();
        //This here is where the api link is used to pick up the information
        HttpResponseMessage response = await client.GetAsync("https://api.openweathermap.org/data/3.0/onecall?lat=33&lon=32&exclude=hourly,daily&appid=e42b8351048e7065fa026c21748e38d4");
        //information on if I can use the api and if the api works
        Console.WriteLine(response);
        Console.WriteLine();
        Console.WriteLine(response.StatusCode);
        if (response.IsSuccessStatusCode)
        {
            // Read the response content
            Console.WriteLine();
            
            // The set up to read the json file
            string responseBody = await response.Content.ReadAsStringAsync();
            JsonDocument jsonDoc = JsonDocument.Parse(responseBody);
            JsonElement root = jsonDoc.RootElement;
            JsonElement current = root.GetProperty("current");

            // Show time
            // Retrieve the timestamp in Unix format
            long unixTimestamp = current.GetProperty("dt").GetInt64();

            // Convert Unix timestamp to DateTimeOffset
            DateTimeOffset dateTimeOffset = DateTimeOffset.FromUnixTimeSeconds(unixTimestamp);
            Console.WriteLine($"Timestamp: {dateTimeOffset.ToString("MM/dd/yyyy HH:mm:ss")}");

            //Below is the responce for the humidity levels
            int humidity = current.GetProperty("humidity").GetInt32();
            Console.WriteLine($"Humidity: {humidity}%");

            //below gets the tempature in both fahreheit and celsius
            //Console.WriteLine(responseBody);
            float temp = current.GetProperty("temp").GetSingle();
            // Coverts Kelvin to Celsius
            float tempCelsius = temp - 273.15f;
            // Convert temperature from Kelvin to Fahrenheit
            float tempFahrenheit = (temp - 273.15f) * 9/5 + 32;
            Console.WriteLine($"Current tempature: {tempCelsius} degrees Celsius and {tempFahrenheit} degrees fahrenheit");

            //what the tempature feels like
            float ftemp = current.GetProperty("feels_like").GetSingle();
            // once again coverts tempature to Celsius
            float ftempCelsius = ftemp - 273.15f;
            // Convert temperature from Kelvin to Fahrenheit
            float ftempFahrenheit = (ftemp - 273.15f) * 9/5 + 32;
            Console.WriteLine($"The tempature feels like: {ftempCelsius} degrees Celsius and {ftempFahrenheit} degrees fahrenheit");

            //gets the wind speed
            float wind = current.GetProperty("wind_speed").GetSingle();
            Console.WriteLine($"The winds are blowing at {wind} MPH");

            // Retrieves how cloudy the skies are
            int clouds = current.GetProperty("clouds").GetInt32();
            Console.WriteLine($"Cloudiness level: {clouds}% goes from 0 to 100%");

            // retrieves the air pressure of the area into PSI
            int pressure = current.GetProperty("pressure").GetInt32();
            float pressurePsi = pressure / 68.9475729f;
            Console.WriteLine($"The air pressure is {pressurePsi}");

            // when the sun will rise
            long epochTime = current.GetProperty("sunrise").GetInt64();
            DateTimeOffset observationTime = DateTimeOffset.FromUnixTimeSeconds(epochTime);
            Console.WriteLine($"Observation time for sunrise: {observationTime.ToString("MM/dd/yy HH:mm")}");

            // when the sun will turn to dusk
            long duskepochTime = current.GetProperty("sunset").GetInt64();
            DateTimeOffset duskobservationTime = DateTimeOffset.FromUnixTimeSeconds(duskepochTime);
            Console.WriteLine($"Observation time for sunset: {observationTime.ToString("MM/dd/yy HH:mm")}");

            // Retrieve visibility in meters
            int visibilityMeters = current.GetProperty("visibility").GetInt32();

            // Convert visibility to kilometers if it's very high
            float visibilityKilometers = visibilityMeters >= 1000 ? visibilityMeters / 1000f : visibilityMeters;
            string visibilityUnit = visibilityMeters >= 1000 ? "km" : "m";
            
            Console.WriteLine($"The Visibility: {visibilityKilometers} {visibilityUnit}");

            // This is the risk of Ultra Violet burns from 1 to 11
            int uv = current.GetProperty("uvi").GetInt32();
            Console.WriteLine($"The current risk of UV burns are at {uv}.");

        }
        
        else
        {
            // If the request was not successful, display the error status code
            Console.WriteLine($"Error: {response.StatusCode}");
        }
    }
} 