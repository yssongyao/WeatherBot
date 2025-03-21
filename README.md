WeatherBot App 

A web-based chatbot application that answers questions about the weather using Python, Flask, HTML, CSS, JavaScript, ChatterBot, and OpenWeather and Geocoding API.

Features 

Chatbot Interaction: Users can interact with the chatbot to ask questions.  
Weather Information: The chatbot can fetch and display weather information for 10 locations in UK using the Geocoding API and OpenWeather API, then answer questions about today or tomorrow or the day after tomorrow's weather for a location, or the 5-day weather forecast for a location.  
Travel suggestion: The chatbot can also suggest when and where to avoid travel due to rainy weather.  

Technologies Used 

Backend: Python, Flask 
Frontend: HTML, CSS, JavaScript 
Chatbot: ChatterBot 
Geo Data: Geocoding API 
Weather Data: OpenWeather API 

requirments.txt 

blis==0.2.4
certifi==2025.1.31
charset-normalizer==3.4.1
ChatterBot==1.0.5
chatterbot-corpus==1.2.2
click==8.1.8
colorama==0.4.6
cymem==2.0.11
exceptiongroup==1.2.2
Flask==2.2.5
idna==3.10
importlib-metadata==6.7.0
iniconfig==2.0.0
itsdangerous==2.1.2
Jinja2==3.1.6
joblib==1.3.2
MarkupSafe==2.1.5
mathparse==0.1.2
murmurhash==1.0.12
nltk==3.8.1
numpy==1.21.6
packaging==24.0
pandas==1.3.5
Pint==0.18
plac==0.9.6
pluggy==1.2.0
preshed==2.0.1
pymongo==3.13.0
pytest==7.4.4
python-dateutil==2.7.5
pytz==2025.1
PyYAML==5.1.2
regex==2024.4.16
requests==2.31.0
six==1.17.0
spacy==2.1.9
SQLAlchemy==1.2.19
srsly==1.0.7
thinc==7.0.8
tomli==2.0.1
tqdm==4.67.1
typing_extensions==4.7.1
urllib3==2.0.7
wasabi==0.10.1
Werkzeug==2.2.3
zipp==3.15.0


Installation 

1. Clone the Repository: 
git clone https://github.com/yssongyao/WeatherBot.git
cd WeatherBot

2. Install Dependencies: 
pip install -r requirements.txt

3. Set Up OpenWeather API Key and Google API key: 

Sign up at OpenWeather and Google to get an API keys.  
Paste your openweather API key in api_key/open_weather_api_key.txt  
Paste your Google API key in api_key/google_api_key.txt.  

Running the App  
1. Start the Flask Server:
python main.py 

2. Access the App:  
Open your browser and navigate to:
http://127.0.0.1:5000 

Code Overview   
 
coordinates.py 
Get the coordinates from Google Geocoding API 

data.py 
Fetching, processing weather data and saving to csv files 

train_data.py 
Processing csv files and saving to various txt files as training data 

main.py 
Creat chatbot and run app 

templates/index.html 
The main HTML file for the frontend 

static/styles.css 
CSS file for styling the app 

Usage   

Ask About the Weather:   

Type: What is the weather in Cambridge? 
The chatbot will display the weather for Cambridge.   
Type: What is the weather in Oxford tomorrow? 
The chatbot will display the weather of tomorrow for Oxford. 

General Chat:   
Type: Hello or How are you? 
The chatbot will respond with a general conversation.
