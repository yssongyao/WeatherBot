from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from data import *
from train_data import *
import asyncio

# Specify the try block.
try:
    # Fetch weather data, process data and save to CSV which need API keys for OpenWeather API and Google Geocoding API
    process_to_csv()
# Specify except block.
except:
    print("Error in fetch data due to no API keys uploaded to a public site. To fix the error, simply add API keys in api_key/google_api_key.txt and api_key/open_weather_api_key.txt")
# Specify finally block.
finally:
    print("Program is executed regardless of API keys; Chatbot can work with pre-loaded data if API keys are removed")


# Asynchronous programming for processing training data into multiple txt files
async def training_data():
   await asyncio.gather(save_today_weather(), # Save today's weather
                        save_tomorrow_weather(), # Save tomorrow's weather
                        save_day_after_tomorrow_weather(), # Save the day after tomorrow's weather
                        save_forecast(), # Save 5-day forecast to forecast.txt
                        save_specific_day(), # Save forecast with specific day Q&A to txt file
                        bad_weather() # Save bad weather data to a txt file
                        )

# Create a chatbot
my_bot = ChatBot(
    name="WeatherBot",
    read_only=True,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation",
                    "chatterbot.logic.BestMatch"],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'
)

# Clear previous training data
print("Clearing previous training data...")
my_bot.storage.drop()

# Math data to train my_bot
training_data_math=open('training_data/math_data.txt').read().splitlines()

# Small talk data to train my_bot
training_data_small_talk=open('training_data/small_talk.txt').read().splitlines()

# guide questions for user to ask in a preferred format for certain keyword such as 'advice' and 'forecast'
training_guide_question=open('training_data/guide_question.txt').read().splitlines()

# Updated weather data for today to train my_bot
today_weather=open('training_data/today.txt').read().splitlines()

# Updated weather data for tomorrow to train my_bot
tomorrow_weather=open('training_data/tomorrow.txt').read().splitlines()

# Updated weather data for the day after tomorrow to train my_bot
day_after_tomorrow_weather=open('training_data/the_day_after_tomorrow.txt').read().splitlines()

# Updated 5-day weather forecast data to train my_bot
forecast_weather=open('training_data/forecast.txt').read().splitlines()

# Updated weather data for specific day Q&A to train my_bot
specific_day_weather=open('training_data/specific_day_weather.txt').read().splitlines()

# Updated bad weather data to train my_bot
bad_weather=open('training_data/bad_weather.txt').read().splitlines()

# Train my_bot with ListTrainer with files saved
print("Training with new data...")
list_trainer = ListTrainer(my_bot)

for item in (training_data_math,
             training_data_small_talk,
             training_guide_question,
             today_weather,
             tomorrow_weather,
             day_after_tomorrow_weather,
             forecast_weather,
             specific_day_weather,
             bad_weather):

    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english') # Train with basic English corpus

# Create a web page to run my_bot

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    return str(my_bot.get_response(user_input))

if __name__=='__main__':
    app.run(debug=False)



