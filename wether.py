import requests
from bs4 import BeautifulSoup


def get_weather(location):
    # Make a request to the Google search results page for the given location.
    url = "https://www.google.com/search?q=weather+{}".format(location)
    response = requests.get(url)

    # Parse the HTML response.
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the temperature and weather details.
    temperature = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    weather_description = soup.find("div", class_="BNeawe tAd8D AP7Wnd").text

    # Return the weather details.
    return {
        "temperature": temperature,
        "weather_description": weather_description,
    }


# weather = get_weather("London")
#
# print(weather)
