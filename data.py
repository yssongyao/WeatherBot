# Import the necessary library
import requests
import pandas as pd
from coordinates import  *

# store open weather api key in txt and read the file
def get_openweather_api_key():
    with open('api_key/open_weather_api_key.txt','r') as file:
        return file.read().strip()

# store the api key in a variable
OPENWEATHER_API_KEY=get_openweather_api_key()

# List of locations in the UK
LOCATIONS = [
    "Cumbria", "Corfe Castle", "The Cotswolds", "Cambridge", "Bristol",
    "Oxford", "Norwich", "Stonehenge", "Watergate Bay", "Birmingham"
]

# Function to fetch 5-day forecast data for a location
def fetch_forecast(location):
    # store coordinates of the location from function in coordinates.py by calling Google Geocoding API
    coord = get_coordinates(location)
    lat = coord[0]
    lon = coord[1]
    # store url for open weather api with params obtained above
    weather_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
    # store response
    response = requests.get(weather_url)
    if response.status_code == 200:
        # store response in json format
        return response.json()
    # error handling
    else:
        print(f"Error fetching weather data for {location}: {response.status_code}")
        return None

# Function to process forecast data and filter one row per day
def process_forecast(data, location):
    forecast_data = []
    for item in data['list']:
        date = item['dt_txt']  # Date and time
        temp = item['main']['temp']  # Temperature
        weather_desc = item['weather'][0]['description']  # Weather description
        humidity = item['main']['humidity'] # Humidity
        wind_speed = item['wind']['speed'] # Wind speed
        forecast_data.append([location, date, temp, weather_desc, humidity, wind_speed])

    # Convert to DataFrame
    df = pd.DataFrame(forecast_data, columns=['Location', 'Date', 'Temperature', 'Weather Description', 'Humidity', 'Wind Speed'])

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract the date part (without time)
    df['Date_Only'] = df['Date'].dt.date

    # Group by date and select the first row for each day
    filtered_df = df.groupby('Date_Only').first().reset_index()

    # Drop the Date column with datetime data
    final_df = filtered_df.drop(filtered_df.columns[2], axis=1)

    # Define a list to store original and processed DataFrames
    df_list = [df, final_df]

    return df_list


# Function to fetch and process data for all locations
def process_to_csv():
    original_data = []
    processed_data = []

    for location in LOCATIONS:
        print(f"Fetching data for {location}...")
        data = fetch_forecast(location)
        if data:
            all_data = process_forecast(data, location)[0]  # [0] to return original dataframe
            original_data.append(all_data)
            filtered_data = process_forecast(data, location)[1] # [1] to return filtered dataframe
            processed_data.append(filtered_data)

    # Combine data for all locations
    combined_df_all = pd.concat(original_data, ignore_index=True)
    combined_df_filtered = pd.concat(processed_data, ignore_index=True)

    # Save to CSV
    combined_df_all.to_csv('data/all_data.csv', index=False)
    combined_df_filtered.to_csv('data/filtered_data.csv', index=False)
    print("Full weather forecast saved to all_data.csv")
    print("Filtered weather saved to filtered_data.csv")


