import requests
import json

base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = '082f01bf2b8b704e3a77ebac94ebbb3d'


def get_current_weather_city(city):
    """units parameter will provide the desired metrics; units=imperial will provide temperature in
    Fahrenheit """
    url = f"{base_url}q={city}&appid={api_key}&units=imperial"
    # print(url)
    response = requests.get(url)  # will provide the full url
    json_data = response.json()  # will provide the data in json format
    # print(json_data)
    temp = json_data["main"]["temp"]
    print(f"The current temperature of the {city.title()} is {temp}")
    min_temp = json_data["main"]["temp_min"]
    print(f"The minimum temperature of the {city.title()} is {min_temp}")
    max_temp = json_data["main"]["temp_max"]
    print(f"The maximum temperature of the {city.title()} is {max_temp}")


def get_current_weather_zip(zip_code):
    """units parameter will provide the desired metrics; units=imperial will provide temperature in
    Fahrenheit """
    url = f"{base_url}zip={zip_code}&appid={api_key}&units=imperial"
    # print(url)
    response = requests.get(url)  # will provide the full url
    json_data = response.json()  # will provide the data in json format
    # print(json_data)
    temp = json_data["main"]["temp"]
    print(f"The current temperature of the {zip_code} is {temp}")
    min_temp = json_data["main"]["temp_min"]
    print(f"The minimum temperature of the {zip_code} is {min_temp}")
    max_temp = json_data["main"]["temp_max"]
    print(f"The maximum temperature of the {zip_code} is {max_temp}")


def main():
    user_input = '0'
    while True:
        # user can terminate the session by entering the 'q'
        user_input = input("Enter Option 1 to find the weather by City or Option 2 to find the Weather by Zip Code or "
                           "Option 'q' to Quit: ")
        if user_input == 'q':
            break

        if user_input != 'q':
            if user_input == '1':
                try:
                    city = input("Enter the Name of the City: ")
                    get_current_weather_city(city)
                except:
                    print("Please Enter the Valid City")

            elif user_input == '2':
                try:
                    zip_code = input("Enter the Zip Code: ")
                    get_current_weather_zip(zip_code)
                except:
                    print("Please Enter the Valid Zip Code")


if __name__ == '__main__':
    main()
