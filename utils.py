import json
from time import sleep
from typing import Optional
from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.by import By


# Convert strings to list, add image into list
def to_list(text: str) -> list[str]:
    lines = text.splitlines()
    return lines


# Create an Album instance and convert it to a dictionary
def to_dict(album: list, holder_dataset: list, dataclass):
    holder_dataset.append(dataclass(*album).__dict__)


# Write holder list into json file
def write_json(data_array: list, path: str):
    with open(path, "w") as file:
        json.dump(data_array, file, indent=4)


# Create instance and navigate to URL
def open_tab(url: str):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


# Scrape all albums on page, return the recently scraped album
def scrape_data(iteration: int, driver) -> list:
    el_xpath = (
        f"/html/body/div[6]/div/div[2]/sections/group[2]/section[3]/div[{iteration}]"
    )
    img_xpath = f"/html/body/div[6]/div/div[2]/sections/group[2]/section[3]/div[{iteration}]/div/a/picture/img"

    element = driver.find_element(By.XPATH, el_xpath)
    img = element.find_element(By.XPATH, img_xpath)

    album_data = to_list(element.text)
    album_data.append(img.get_attribute("src"))

    return album_data
