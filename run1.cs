using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using var client = new HttpClient();
        HttpResponseMessage response = await client.GetAsync("https://api.example.com/data");
        if (response.IsSuccessStatusCode)
        {
            // Read the response content
            string responseBody = await response.Content.ReadAsStringAsync();
            Console.WriteLine(responseBody);
        }
        else
        {
            // If the request was not successful, display the error status code
            Console.WriteLine($"Error: {response.StatusCode}");
        }
    }
} 