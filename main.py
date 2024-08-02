from time import sleep
from dataclasses import dataclass

from utils import to_list, to_dict, write_json

from selenium import webdriver
from selenium.webdriver.common.by import By


# define class
@dataclass
class Album:
    title: str
    artist: str
    average: str
    ratings: str
    reviews: str
    date: str
    main_genre: str
    sub_genre: str
    description: str


# define varibles
holder_array = []

PATH = "/album_data.json"

running = True  # create a bool to know when we're running

driver = webdriver.Chrome()  # create instance of chrome

URL = "https://rateyourmusic.com/charts/top/album/all-time/deweight:live,archival,soundtrack/"  # navigate to website


# start the scrape
while running:
    driver.get(URL)

    sleep(20)

    # start scraping data
    for i in range(1, 5):
        # Get the xpath of the elemnts
        el_xpath = f"/html/body/div[6]/div/div[2]/sections/group[2]/section[3]/div[{i}]"
        img_xpath = f"/html/body/div[6]/div/div[2]/sections/group[2]/section[3]/div[{i}]/div/a/picture/img"

        # define the elements
        element = driver.find_element(By.XPATH, el_xpath)
        # img = element.find_element(By.XPATH, img_xpath)

        # place the data into list
        album_data = to_list(element.text)

        # convert to dictionary
        to_dict(album_data, holder_array, Album)
        sleep(5)

    # once data is scraped, place it into json file
    write_json(holder_array, PATH)

    running = False

sleep(10)  # wait a lil

# close the browser
driver.close()
