import os
from main import training_data

def test_train_chatbot():
    get_training_data = training_data()
    assert get_training_data is not None
    assert os.path.exists('training_data/today.txt')
    assert os.path.exists('training_data/tomorrow.txt')
    assert os.path.exists('training_data/the_day_after_tomorrow.txt')
    assert os.path.exists('training_data/forecast.txt')
    assert os.path.exists('training_data/specific_day_weather.txt')
    assert os.path.exists('training_data/bad_weather.txt')