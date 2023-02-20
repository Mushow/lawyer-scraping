import asyncio
import re
import time
from Lawyer import Lawyer
import aiohttp
import pandas as pd
from bs4 import BeautifulSoup


async def get_links(session, url):
    async with session.get(url) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')
        cards = soup.find_all('div', class_='entry-content')
        return [card.find('a').get('href') for card in cards]


def get_clean_text(text):
    return re.sub(' +', ' ', text.get_text(strip=True))


async def get_lawyer(session, link):
    async with session.get(link) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')
        nameElement = soup.find('header', class_='entry-header')
        numberElement = soup.find('div', class_='entry-infos__item--tel')
        emailElement = soup.find('div', class_='entry-infos__item--mail')
        subsequentInformation = soup.findAll('div', class_='entry-content__item')

        try:
            name = get_clean_text(nameElement.find('h1'))
            number = get_clean_text(numberElement.find('a'))
            email = get_clean_text(emailElement.find('a'))
            cases = swornDate = address = postalCode = None
            for info in subsequentInformation:
                key = info.find('b').text
                match key:
                    case "Case":
                        cases = get_clean_text(info.find('p'))
                    case "Prestation de serment":
                        swornDate = get_clean_text(info.find('p'))
                    case "Rue":
                        address = get_clean_text(info.find('p')).replace(" ", " ")
                    case "Code postal":
                        postalCode = get_clean_text(info.find('p')).upper()

            return Lawyer(name, number, email, cases, swornDate, address, postalCode)
        except AttributeError:
            pass


def format_lawyers(lawyers_array):
    lawyers_data = []
    for lawyer in lawyers_array:
        if lawyer:
            lawyer_dict = {
                'Name': lawyer.get_name(),
                'Phone': lawyer.get_number(),
                'Cases': lawyer.get_cases(),
                'Email': lawyer.get_email(),
                'Address': lawyer.get_address(),
                'Sworn Date': lawyer.get_sworn_date(),
                'City': lawyer.get_city()
            }
            lawyers_data.append(lawyer_dict)

    return lawyers_data


async def main():
    baseUrl = "https://www.barreaulyon.com"
    uri = "/annuaire?paged="

    async with aiohttp.ClientSession() as session:
        links_tasks = []
        lawyers_tasks = []
        for pageNb in range(1, 333+1):
            url = baseUrl + uri + str(pageNb)
            links_tasks.append(get_links(session, url))

        links = await asyncio.gather(*links_tasks)
        links_array = [link for page in links for link in page]

        for link in links_array:
            lawyers_tasks.append(get_lawyer(session, link))

        lawyers_array = await asyncio.gather(*lawyers_tasks)

        lawyers_data = format_lawyers(lawyers_array)

        df = pd.DataFrame(lawyers_data)
        df = df.sort_values('Cases', ascending=False)
        df.to_csv('lawyers.csv', index=False)

        return lawyers_data


if __name__ == '__main__':
    tic = time.perf_counter()
    lawyers = asyncio.run(main())
    toc = time.perf_counter()
    print(f"Retrieved {len(lawyers)} lawyers in {toc - tic:0.4f} seconds")
