from geopy.geocoders import Nominatim  # This is needed for zipcode to lat, long conversion
import requests  # This is needed to use the weather api
import re  # This is needed for the regex and validate the zipcode
import sys  # This is needed to terminate the python program in case something goes wrong with the weather data.


def zipcode_to_coordinates(zipcode):
  # Simple function to convert zipcode to coordinates
  # It uses the Nominatim geolocator service, with the user_agent jc-weather-app-final (apparently the user_agent can be anything)

  geolocator_service = Nominatim(user_agent="jc-weather-app-final")

  # This basically makes a call to the Nominatim service putting the zipcode we provided in order to return some coordinates
  location = geolocator_service.geocode(zipcode)

  # The nominatim service (method really) returns None if it fails
  if location is not None:
    #If it doesnt fail then return the lat and long
    return location.latitude, location.longitude
    # Else return None
  return None


def c_to_f(c):
  # Simple conversion of Celsius to Fahrenheit.
  # Takes c as a parameter and returns f.
  # Round to two decimal places to avoid long running float values.
  return round((c * 9 / 5) + 32, 2)


def validate_zipcode(zipcode):
  # This is very very very poor zipcode validation, but it's okay for now because the validation can get very complicated and it will throw off the time for this project a bit too much.

  # Check if the zipcode is length of 5, if it is not then return False
  if len(zipcode) != 5:
    return False
    # Do a re.match to see if it matches exactly 5 digits, if the match fails it will return None, if is None then it will return false, else true
  return re.match(r"^\d{5}$", zipcode) is not None


def get_and_print_weather_data(latitude, longitude):
  # A simple function that takes lat and long values and it uses open-meteo url/api to get weather values.

  # I am specifically asking for some values like, daily min, max temp, sunrise
  response = requests.get(
      f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,daylight_duration&forecast_days=1"
  )

  # To be able to use the data as a object/dictionary we must do response.json() it takes the content of the response and makes it a dictionary.
  data = response.json()
  # If the request succeeds, we want to fetch / print some tempt values
  if response.status_code == 200:

    # In here I am grabbing different values, from temperature, also the smallest and maximum (many of the values are just in a list matching hourly values)

    # Here I am grabbing min temp by using the method min (which takes the minimum value from a list) and rounding them to 2 decimal places to avoid long running float values.
    min_temperature_c = round(min(data['hourly']['temperature_2m']), 2)
    # Now I am grabbing the max temp value by using the max method, which takes the maximum value of the list, also rounding to 2 decimal places.
    max_temperature_c = round(max(data['hourly']['temperature_2m']), 2)

    # Now I convert both values to F to display it to the people interested in F values.
    min_temperature_f = c_to_f(min_temperature_c)
    max_temperature_f = c_to_f(max_temperature_c)

    # Now we take the daily min and max temperature in C and rounding it to 2 decimal places.
    min_daily_temperature_c = round(data['daily']['temperature_2m_min'][0], 2)
    max_daily_temperature_c = round(data['daily']['temperature_2m_max'][0], 2)
    # Now we also convert those to F for the users interested in F values.
    min_daily_temperature_f = c_to_f(min_daily_temperature_c)
    max_daily_temperature_f = c_to_f(max_daily_temperature_c)

    # Now we print a summary of the forecast, each print statement contains some information about the forecast or a message.
    print(
        f"\nForecast for {data['daily']['time'][0]} (Latitude: {data['latitude']}, Longitude: {data['longitude']})"
    )
    print(f"- Timezone: {data['timezone']}")
    print("\nHourly Forecast Summary:")
    print(
        f"- Temperature ranges from {min_temperature_c}°C ({min_temperature_f}°F) to {max_temperature_c}°C ({max_temperature_f}°F)"
    )
    print(
        f"Precipiatation Probability: {max(data['hourly']['precipitation_probability'])}% (This always seems a bit off for some reason)"
    )
    print("\nDaily Forecast Details:")
    print(
        f"- Maximum temperature: {max_daily_temperature_c}°C ({max_daily_temperature_f}°F)"
    )
    print(
        f"- Minimum temperature: {min_daily_temperature_c}°C ({min_daily_temperature_f}°F)"
    )
    print(
        f"- Sunrise at {data['daily']['sunrise'][0]}, Sunset at {data['daily']['sunset'][0]}"
    )
    print(
        f"- Daylight duration: {data['daily']['daylight_duration'][0]/3600:.2f} hours"
    )
    print(
        "Thank you for using this program! Please be mindful about its usage as it is powered by free services, any abuse of this program will probably end up on it being blocked and unable to keep providing this amazing and accurate (sometimes) weather data.\n\nPlease feel free to rerun the program if you want to check the weather again!"
    )

  else:
    # This is sent if the weather api from open-meteo somehow fails or something.
    print("Whoops, something went wrong. Please try again later.")
    sys.exit(0)


def main():

  print("""Welcome to Jorge's Weather Forecast! Enter your zipcode to begin\n
  \nCurrently it only supports zipcodes in a 5 digit format (10010 for example).
        """)

  # We set a flag to keep running the loop until we want to.
  run = 1
  # This is used to know if the user has already ran the program.
  count = 0

  while run == 1:  # We start the while loop.

    # If it is the user's first time we show this.
    if count == 0:
      zipcode = input("\nEnter your zipcode: ")
      # Add one to counter so we know that the user has already ran the program before.
      count += 1
    else:
      #If the user has already ran the program we want to give this option now to leave, in case their zip-code doesnt work.
      zipcode = input(
          "\nEnter your zipcode:  - or enter 'done' to end the program\n ")
      if zipcode == "done":
        #If the user enters to finish the program then we leave.
        print("Bye!")  # print a bye
        # set the flag to 0, so now the while loop will stop.
        run = 0
        break  # break out of the loop just in case.
    if not validate_zipcode(zipcode):
      #If the user doesn't enter a valid zipcode then we print this and continue until the user leaves or enter a valid zipcode
      print("\nInvalid zipcode. Please enter a 5-digit zipcode (e.g., 10010).")
      continue

      # We declare the coordinates from the returning value of the zipcode_to_coordinates, at this point it is assumed that the zipcode is valid.
    coordinates = zipcode_to_coordinates(zipcode)

    if coordinates is not None:
      #If the coordinates are valid, meaning the zipcode was probably valid as well.
      get_and_print_weather_data(
          coordinates[0], coordinates[1]
      )  #Now we pass the lat and long values to the get_and_print_weather_data so it will print the forecast information.
      run = 0  # Change the flag to 0 so the while loop will stop.
      print("Bye!")  # say bye uwu
      break


if __name__ == '__main__':
  main()  # We call the main function to start the program.
