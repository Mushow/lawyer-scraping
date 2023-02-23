import asyncio
import re
import time

import aiohttp
import pandas as pd
from bs4 import BeautifulSoup

import csvUtils
from Lawyer import Lawyer


async def get_links(session, url):
    async with session.get(url) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')
        cards = soup.find_all('div', class_='entry-content')
        return [card.find('a').get('href') for card in cards]


def get_clean_text(text):
    return re.sub(' +', ' ', text.get_text(strip=True))


def to_date(sworn_date):
    months = {
        "janvier": 1,
        "février": 2,
        "mars": 3,
        "avril": 4,
        "mai": 5,
        "juin": 6,
        "juillet": 7,
        "août": 8,
        "septembre": 9,
        "octobre": 10,
        "novembre": 11,
        "décembre": 12
    }

    day, month_name, year = sworn_date.split()
    month = months[month_name]
    date = f"{day}/{month:02d}/{year}"

    return date


async def get_lawyer(session, link):
    async with session.get(link) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')
        name_element = soup.find('header', class_='entry-header')
        number_element = soup.find('div', class_='entry-infos__item--tel')
        email_element = soup.find('div', class_='entry-infos__item--mail')
        subsequent_information = soup.findAll('div', class_='entry-content__item')

        try:
            name = get_clean_text(name_element.find('h1'))
            number = get_clean_text(number_element.find('a'))
            email = get_clean_text(email_element.find('a'))
            cases = sworn_date = address = postal_code = None
            for info in subsequent_information:
                key = info.find('b').text
                match key:
                    case "Case":
                        cases = get_clean_text(info.find('p'))
                    case "Prestation de serment":
                        sworn_date = get_clean_text(info.find('p'))
                    case "Rue":
                        address = get_clean_text(info.find('p')).replace(" ", " ")
                    case "Code postal":
                        postal_code = get_clean_text(info.find('p')).upper()

            if cases or sworn_date or address or postal_code is None:
                pass

            return Lawyer(name, number, email, cases, to_date(sworn_date), address, postal_code)
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


def sort_df(df, value):
    df = df.sort_values(value, ascending=True)
    return df


async def main():
    baseUrl = "https://www.barreaulyon.com/"
    uri = "annuaire?paged="
    lastPage = 333

    async with aiohttp.ClientSession() as session:
        links_tasks = []
        lawyers_tasks = []
        for pageNb in range(1, lastPage + 1):
            url = baseUrl + uri + str(pageNb)
            links_tasks.append(get_links(session, url))

        links = await asyncio.gather(*links_tasks)
        links_array = [link for page in links for link in page]

        for link in links_array:
            lawyers_tasks.append(get_lawyer(session, link))

        lawyers_array = await asyncio.gather(*lawyers_tasks)

        lawyers_data = format_lawyers(lawyers_array)

        df = pd.DataFrame(lawyers_data)
        df = sort_df(df, 'Cases')
        print(df.values.tolist())
        df = csvUtils.nullToZero(df, 'Cases')

        keywords = ['city', 'address', 'sworn date']

        for col in df.columns:
            if any(keyword in col.lower() for keyword in keywords):
                df = csvUtils.nullToUnknown(df, col)

        df = csvUtils.dropNull(df, ['Phone', 'Email'])

        df.to_csv('lawyers.csv', index=False)

        return lawyers_data

if __name__ == '__main__':
    tic = time.perf_counter()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    lawyers = asyncio.run(main())
    toc = time.perf_counter()
    print(f"Retrieved {len(lawyers)} lawyers in {toc - tic:0.4f} seconds")
