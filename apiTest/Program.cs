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
        Console.WriteLine(response);
        Console.WriteLine();
        Console.WriteLine(response.StatusCode);
        if (response.IsSuccessStatusCode)
        {
            // Read the response content
            Console.WriteLine();
            //Below is the responce for the humidity levels
            string responseBody = await response.Content.ReadAsStringAsync();
            JsonDocument jsonDoc = JsonDocument.Parse(responseBody);
            JsonElement root = jsonDoc.RootElement;
            JsonElement current = root.GetProperty("current");
            int humidity = current.GetProperty("humidity").GetInt32();
            Console.WriteLine($"Humidity: {humidity}%");
            //below gets the tempature
            //JsonElement temp = root.GetProperty("temp");
            Console.WriteLine(responseBody);
            //int temp = current.GetProperty("temp").GetInt32();
            //Console.WriteLine($"Current tempature: {temp} degrees");
        }
        
        else
        {
            // If the request was not successful, display the error status code
            Console.WriteLine($"Error: {response.StatusCode}");
        }
    }
} 