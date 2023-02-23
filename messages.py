error_prefix = "[Error]"
success_prefix = "[Success] "
error_response = "Response hasn't been able to be received"
dictionnary_conversion = "The list of object was correctly converted to a dictionnary"
starting = "Starting to scrape...\n"
exporting = "Exporting...\n"
scraping_page_start = "Page N°"
scraping_page_end = "has been scraped"
links = "The links have been correctly retrieved"
done = "Done!"


def response_error():
    print(error_prefix, error_response)


def page_success(pageNumber):
    print(success_prefix, scraping_page_start, str(pageNumber), scraping_page_end)


def finished_success():
    print(done)


def success_links():
    print(success_prefix, links)


def dictionnary_conversion_success():
    print(success_prefix, dictionnary_conversion)


def export():
    print(exporting)


def starting_scraping():
    print(starting)
