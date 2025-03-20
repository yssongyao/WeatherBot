# Import the necessary library
import csv
from datetime import datetime, timedelta
from data import *


# Process filtered_data.csv and save today's weather to today.txt
async def save_today_weather():
    today = datetime.now().strftime('%Y-%m-%d')
    with open('data/filtered_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        today_data = [row for row in reader if row['Date_Only'].startswith(today)]

    with open('training_data/today.txt', 'w') as txtfile:
        for row in today_data:
            txtfile.write(f"What is the weather in {row['Location']} today?\n")
            txtfile.write(f"The weather in {row['Location']} today is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")
            txtfile.write(f"How is the weather in {row['Location']} today?\n")
            txtfile.write(f"The weather in {row['Location']} today is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")
            txtfile.write(f"weather in {row['Location']} today\n")
            txtfile.write(f"The weather in {row['Location']} today is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")

# Process filtered_data.csv and save tomorrow's weather to tomorrow.txt
async def save_tomorrow_weather():
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    with open('data/filtered_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        tomorrow_data = [row for row in reader if row['Date_Only'].startswith(tomorrow)]

    with open('training_data/tomorrow.txt', 'w') as txtfile:
        for row in tomorrow_data:
            txtfile.write(f"What is the weather in {row['Location']} tomorrow?\n")
            txtfile.write(f"The weather in {row['Location']} tomorrow is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")
            txtfile.write(f"How is the weather in {row['Location']} tomorrow?\n")
            txtfile.write(f"The weather in {row['Location']} tomorrow is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")
            txtfile.write(f"weather in {row['Location']} tomorrow\n")
            txtfile.write(f"The weather in {row['Location']} tomorrow is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")

# Process filtered_data.csv and save weather data for the day after tomorrow to a txt file
async def save_day_after_tomorrow_weather():
    day_after_tomorrow = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    with open('data/filtered_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        after_tomorrow_data = [row for row in reader if row['Date_Only'].startswith(day_after_tomorrow)]

    with open('training_data/the_day_after_tomorrow.txt', 'w') as txtfile:
        for row in after_tomorrow_data:
            txtfile.write(f"What is the weather in {row['Location']} the day after tomorrow?\n")
            txtfile.write(f"The weather in {row['Location']} the day after tomorrow is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")
            txtfile.write(f"How is the weather in {row['Location']} the day after tomorrow?\n")
            txtfile.write(f"The weather in {row['Location']} the day after tomorrow is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")
            txtfile.write(f"weather in {row['Location']} for the day after?\n")
            txtfile.write(f"The weather in {row['Location']} for the day after tomorrow is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")
            txtfile.write(f"weather in {row['Location']} the day after?\n")
            txtfile.write(f"The weather in {row['Location']} for the day after tomorrow is {row['Weather Description']} with a temperature of {row['Temperature']}°C, humidity of {row['Humidity']}%, and wind speed of {row['Wind Speed']} m/s.\n")

# Process filtered_data.csv and save 5-day forecast to forecast.txt
async def save_forecast():
    with open('data/filtered_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open('training_data/forecast.txt', 'w') as txtfile:

        # Add Q&A to guide user ask question in preferred format and saved to training_data/guide_question.txt

        # Save forecast Q&A pairs to txt
        for location in LOCATIONS:
            forecast_data = [row for row in rows if row['Location'] == location]
            txtfile.write(f"What is the weather forecast for {location}?\n")
            for row in forecast_data:
                txtfile.write(f"{row['Date_Only']}: {row['Weather Description']}, {row['Temperature']}°C, {row['Humidity']}%, {row['Wind Speed']} m/s;    ")
            txtfile.write("\n")
            txtfile.write(f"Can you give me weather forecast for {location}?\n")
            for row in forecast_data:
                txtfile.write(
                    f"{row['Date_Only']}: {row['Weather Description']}, {row['Temperature']}°C, {row['Humidity']}%, {row['Wind Speed']} m/s;    ")
            txtfile.write("\n")
            txtfile.write(f"weather forecast for {location}?\n")
            for row in forecast_data:
                txtfile.write(f"{row['Date_Only']}: {row['Weather Description']}, {row['Temperature']}°C, {row['Humidity']}%, {row['Wind Speed']} m/s;    ")
            txtfile.write("\n")
            txtfile.write(f"forecast for {location}?\n")
            for row in forecast_data:
                txtfile.write(
                    f"{row['Date_Only']}: {row['Weather Description']}, {row['Temperature']}°C, {row['Humidity']}%, {row['Wind Speed']} m/s;    ")
            txtfile.write("\n")


# Process filtered_data.csv and save Q&A about weather for a specific day to a txt file
async def save_specific_day():
    with open('training_data/specific_day_weather.txt', 'w') as file:
        with open('data/filtered_data.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip header
            for row in reader:
                date, location, temp, weather, humidity, wind_speed = row
                file.write(f"What is the weather in {location} on {date}?\n")
                file.write(f"The weather in {location} on {date} is {weather} with a temperature of {temp}°C, humidity of {humidity}%, and wind speed of {wind_speed} m/s.\n")
                file.write(f"What's weather in {location} on {date}?\n")
                file.write(f"The weather in {location} on {date} is {weather} with a temperature of {temp}°C, humidity of {humidity}%, and wind speed of {wind_speed} m/s.\n")
                file.write(f"How is the weather in {location} on {date}?\n")
                file.write(f"The weather in {location} on {date} is {weather} with a temperature of {temp}°C, humidity of {humidity}%, and wind speed of {wind_speed} m/s.\n")
                file.write(f"Weather in {location} on {date}?\n")
                file.write(f"The weather in {location} on {date} is {weather} with a temperature of {temp}°C, humidity of {humidity}%, and wind speed of {wind_speed} m/s.\n")

# Process all_data.csv and save bad weather data to a txt file
async def bad_weather():

    # filter rainy data to a csv file
    df = pd.read_csv("data/all_data.csv")

    # Filter rows where the "Weather Description" column contains the keyword "rain" (case-insensitive)
    keyword = 'rain'
    rain_df = df[df['Weather Description'].str.contains(keyword, case=False)]
    rain_df.to_csv('data/rain.csv', index=False)
    print("Bad weather saved to rain.csv")

    # design travel advice Q&A pairs and save to txt
    with open('data/rain.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open('training_data/bad_weather.txt', 'w') as txtfile:

        # Add Q&A to guide user ask question in preferred format and saved to training_data/guide_question.txt

        # save formatted Q&A to txt
        for location in LOCATIONS:
            forecast_data = [row for row in rows if row['Location'] == location]
            txtfile.write(f"rainy day and time for {location}?\n")
            for row in forecast_data:
                txtfile.write(
                    f"{row['Date']}: {row['Weather Description']}  ")
            txtfile.write("\n")




