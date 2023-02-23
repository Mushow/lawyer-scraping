import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

import messages
from Lawyer import Lawyer

base_url = "https://www.barreaulyon.com"
uri = "/annuaire?paged="
final_url = base_url + uri
total_pages = 15


def swoup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml') if response.ok else messages.response_error() and None


def get_links():
    return [final_url + str(page) for page in range(1, total_pages + 1)]


def get_page_from_url(page):
    return page.split("=")[1]


def success_soup(page):
    messages.success_links()
    messages.page_success(get_page_from_url(page))


def find_lawyer_cards(soup):
    return soup.findAll("div", class_="entry-content")


def clean_text(text):
    return re.sub(' +', ' ', text.get_text(strip=True)).replace(" ", " ").replace("\n", "").replace(" - -", "")


def get_info(card, class_name):
    return clean_text(card.find("p", class_=class_name)) if card.find("p", class_=class_name) else None


def get_card_info(card):
    class_names = [
        "entry-title",
        "card-annuaire__info--tel",
        "card-annuaire__info--mail",
        "card-annuaire__info--adress",
        "card-annuaire__info--website",
    ]

    info_values = (get_info(card, class_name) for class_name in class_names)
    return Lawyer(*info_values)


def format_lawyers(lawyers_array):
    lawyers_data = []
    for lawyer in lawyers_array:
        if lawyer:
            website = lawyer.get_website()
            lawyer_dict = {
                'Name': lawyer.get_name(),
                'Number': lawyer.get_number(),
                'Email': lawyer.get_email(),
                'Address': lawyer.get_address(),
                'Website': lawyer.get_website()
            }
            lawyers_data.append(lawyer_dict)
    messages.dictionnary_conversion_success()

    return lawyers_data


def main():
    messages.starting_scraping()
    lawyers = [get_card_info(card) for page in get_links() if (soup := swoup(page)) for card in find_lawyer_cards(soup)]
    lawyers = format_lawyers(lawyers)
    messages.export()
    pd.DataFrame(lawyers).to_csv("lawyers.csv", index=False)
    messages.finished_success()


main()
