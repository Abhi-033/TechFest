import requests
from uagents import Agent, Protocol, Model
import time
import tkinter as tk
from tkinter import ttk
from uagents.setup import fund_agent_if_low
from plyer import notification

class TemperatureData(Model):
    location: str
    temperature: float

temperature_protocol = Protocol("TemperatureProtocol")

class TemperatureAlertAgent(Agent):
    def __init__(self, location):
        super().__init__(name="TemperatureAlertAgent",endpoint=["http://127.0.0.1:8000/submit"])
        self.location = location
    def get_current_temperature(self):
            API_KEY = ''
            API_URL = 'https://api.openweathermap.org/data/2.5/weather'
            params = {
            'q': location,
            'appid': API_KEY,
            'units': 'metric' 
            }
            response = requests.get(API_URL, params=params).json()
            if 'main' in response and 'temp' in response['main']:
                return response['main']['temp']
            return None

location =input("Enter Location: ") 
temperature_alert_agent = TemperatureAlertAgent(location=location)
if __name__ == "__main__":
    current_temp = temperature_alert_agent.get_current_temperature()

    min_temperature=float(input("Enter Minimum Temperature: "))
    max_temperature=float(input("Enter Maximum Temperature: "))
    
    fund_agent_if_low(temperature_alert_agent.wallet.address())

    while True:
        if current_temp is not None:
            print(f'Current temperature in {location}: {current_temp}°C')
            
            if current_temp < min_temperature:
                alert_message = f'Temperature is below the minimum threshold ({min_temperature}°C). Sending alert...'
                print(alert_message)
                notification.notify(
                    title="Temperature Alert",
                    message=alert_message,
                    app_name="TemperatureAlert"
                )
            
            if current_temp > max_temperature:
                alert_message = f'Temperature is above the maximum threshold ({max_temperature}°C). Sending alert...'
                print(alert_message)
                notification.notify(
                    title="Temperature Alert",
                    message=alert_message,
                    app_name="TemperatureAlert"
                )
        time.sleep(3)

temperature_alert_agent.run()
