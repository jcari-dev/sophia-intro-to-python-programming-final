# Sophia: Introduction to Python Programming Final Project

Welcome to my capstone project for the "Introduction to Python Programming" course offered by Sophia Learning. This project, a practical Python application, offers a user-friendly interface to retrieve weather forecasts using zip codes.

## Project Overview

**Weather App:** A concise yet potent application allowing users to input a zip code and receive a detailed weather forecast for the corresponding location. The application translates the zip code into geographic coordinates, which are then used to fetch weather data from a public API.

### Features
- **Zip Code to Coordinates Conversion:** Leverages the `geopy` library to convert zip codes into latitude and longitude.
- **Weather Forecast Retrieval:** Utilizes the `requests` library to fetch weather data from the Open-Meteo API based on the geographic coordinates.
- **User-Friendly Interface:** Simple input and output design, making it easy for users to get weather forecasts.

### Score and Recognition
This project was honored with a **98/100** score, highlighting its excellence in code quality, application functionality, and user experience. _It is an Intro class, ok? but they're awesome!_

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. This application requires the following Python libraries:
- `geopy`
- `requests`

You can install these libraries using pip:

```bash
pip install geopy requests
```

### Setup and Usage
1. **Clone the Repository:** Clone this repository to your local machine to get started.
2. **Run the Application:** Navigate to the directory containing the app and run it using Python:

```bash
python weather_app.py
```

3. **Enter a Zip Code:** Follow the prompts and input a 5-digit zip code when requested.

## Contribution
Your contributions are welcome! Whether it's suggesting new features, improving the code, or reporting bugs, feel free to fork this repository and submit your pull requests. Let's make this weather app even better together.

## Acknowledgements
- Sophia Learning for providing an excellent learning platform.
- Open-Meteo for offering a reliable and free weather data API.

Thank you for your interest in this project! Enjoy exploring Python programming through this practical application.
