# Weather-GUI
**🌤️ Weather App 🌍**


**📜 Overview**_
This is a simple weather application built using Python and Tkinter for the graphical user interface. The app provides weather information by fetching data from the OpenWeatherMap API. You can enter the city name, and it will display real-time weather details such as temperature 🌡️, wind speed 🌬️, humidity 💧, pressure 🧑‍🔬, and weather description 🌥️. The app also provides local time 🕰️ and adjusts based on the city's timezone.



**🌟 Features**

- Real-Time Weather Information 🌡️: Displays the current temperature, wind speed, humidity, pressure, and weather description for a specific city.

- City Search 🔍: Enter the city name to fetch weather details.

- Timezone Integration ⏰: The app fetches and displays local time for the entered city.

- Error Handling ⚠️: Displays user-friendly error messages for invalid inputs or failed network requests.

- Visual Design 🎨: The app includes images for better presentation, including a logo, search icon, and custom background.

**🛠️ Requirements**

- To run this weather app, make sure you have the following installed:

- Python 3.x: You can download Python from https://www.python.org/downloads/.

- Geopy: pip install geopy

- Requests: pip install requests

- TimezoneFinder: pip install timezonefinder

- Pytz: pip install pytz

**🎮 How to Use**


Enter a City Name 🏙️:

- Use the text field to type the name of the city whose weather you want to check.

- Click the Search Button 🔍:

- Press the search icon to fetch the weather data for the entered city.

View Weather Information 🌡️:

- The app will display temperature, wind speed, humidity, pressure, and weather description.

**Local Time ⏰:**

- The current local time of the entered city will be displayed.

**📸 Visuals**
Here is an example of the app interface:

- Weather Data: Shows temperature, wind speed, humidity, etc.

- Search: A search bar to enter a city name.

- Logo: Displays the app's logo for branding.

- Clock: Shows the current time for the selected city.
**
**🔧 How It Works
- User Input: The user enters a city name in the text field.

- Location Fetching: The app uses the Geopy API to get the coordinates (latitude and longitude) of the entered city.

Timezone Calculation: The TimezoneFinder API is used to find the local timezone of the city.

- Weather API: The app fetches weather data using the OpenWeatherMap API by providing the city name.

- Data Display: The weather data (temperature, wind speed, humidity, etc.) is displayed on the app interface.

**📝 Error Handling**

- Invalid City Name: If the city is not found, an error message will pop up prompting the user to enter a valid city.

- Network Issues: If there’s a network error or no internet connection, the app will show a message to check the connection.
**
💾 Files and Icons**

- search.png: Search bar icon.

- search_icon.png: Button icon for triggering the weather search.

- logo.png: Application logo.

- box.png: Background frame image for the interface.

**🎨 App Interface**

- City Search: Input field to enter the city's name.

- Weather Display: Labels showing real-time weather data.

- Local Time: Current time based on the selected city.

- Buttons: A search icon to trigger the weather update.

