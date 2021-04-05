import Minecraft.world.weather as _weather

Weather = _weather.Weather

def register_weather(s, weather):
    _weather.weather.setdefault(s, weather)
