import requests
from bs4 import BeautifulSoup

# Setting the base URL
URL = "https://www.imdb.com/list/ls026253657/"
# Initializing the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
}

# The main function
def check_movies():
    # Getting the page
    page = requests.get(URL, headers=headers)
    # Creating the BeautifulSoup object
    soup = BeautifulSoup(page.content, 'html.parser')
    # The title and the genere
    title = soup.find('h3', class_="lister-item-header")
    for x in title.find_all('a'):
        print(x.text)
        # Appending to the file
        with open('movies.txt', 'a') as f:
            f.write(str(x.text))

# Calling the function-
check_movies()