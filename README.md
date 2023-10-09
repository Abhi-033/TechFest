# Temperature Alert System

## Overview

The TechFest Temperature Alert System is a Python application that monitors the temperature in a specified location and sends alerts when the temperature falls below or rises above certain thresholds.

## Features

- Retrieves current temperature data from the OpenWeatherMap API.
- Allows users to set minimum and maximum temperature thresholds.
- Sends notifications when temperature thresholds are exceeded.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.10 or higher installed.
- uAgents Libraries.
- A virtual environment (optional but recommended).
- A valid API key for the OpenWeatherMap API. You can obtain one by following the instructions below.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/YourUsername/TechFest.git

2. Navigate to the project directory:
   ```bash
   cd TechFest

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv



## Activate the virtual environment:
1. on Windows
   ```bash
   .\venv\Scripts\activate


## API_key
1. Create an APP_KEY.py program in the project directory with the following code to retrieve the API key from the .env file:
   ```python
    
    from dotenv import load_dotenv
    import os
    
    load_dotenv()
    
    API_KEY = os.getenv("API_KEY")
    
    print("API_KEY",API_KEY)   




1. Run the application:
   ```bash
   cd TechFest


## Usage

Upon running the application, 
you will be prompted to enter the location, minimum temperature threshold, and maximum temperature threshold.
The application will continuously monitor the temperature in the specified location and provide alerts when thresholds are exceeded.



