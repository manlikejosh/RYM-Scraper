from time import sleep
from typing import Optional
from dataclasses import dataclass


from utils import to_list, to_dict, write_json, open_tab, scrape_data

from selenium import webdriver
from selenium.webdriver.common.by import By


# define class
@dataclass
class Album:
    title: str = "no title"
    artist: str = "no artist"
    average: str = "no average"
    ratings: str = "no ratings"
    reviews: str = "no reviews"
    date: str = "no date"
    main_genre: str = "no main genre"
    sub_genre: str = "no sub genre"
    description: str = "no description"
    img_url: Optional[str] = None


# define varibles
holder_array = []

PATH = "rym_scraper/albums.json"

running = True  # create a bool to know when we're running

urls = [
    "https://rateyourmusic.com/charts/top/album/all-time/deweight:live,archival,soundtrack/",
    "https://rateyourmusic.com/charts/top/album/all-time/deweight:live,archival,soundtrack/2/",
    "https://rateyourmusic.com/charts/top/album/all-time/deweight:live,archival,soundtrack/3/",
]

count = 0

# start the scrape
while running:
    for url in urls:
        driver = open_tab(url)

        sleep(20)

        # scrape the page data
        for i in range(1, 41):

            # scrape the data into temp array
            this_album = scrape_data(i, driver)

            # convert to dictionary
            to_dict(this_album, holder_array, Album)

            sleep(5)  # wait a lil

            print(f"album {i} is done")

        count += 1

        print(f"page {count} is done")

        # close browser
        driver.close()

        sleep(10)  # wait a lil

    running = False

# once data is scraped, place it into json file PLACE INTO OUTER LOOP
print("all albums are done")
write_json(holder_array, PATH)
