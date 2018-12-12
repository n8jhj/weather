import os
import json

DEFAULT_SAVE_PATH = os.path.join('library', 'data.json')

class WeatherApp:
    def get_data(self):
        return dict(temperature=25, humidity=0.5)

    def save(self, data, save_path=DEFAULT_SAVE_PATH):
        with open('data.json', 'w') as jf:
            json.dump(data, jf)
        os.renames('data.json', save_path)
