error_prefix = "[Error]"
success_prefix = "[Success] "
error_response = "Response hasn't been able to be received"
scraping_page_start = "Page N°"
scraping_page_end = "has been scraped"
links = "The links have been correctly retrieved"
done = "Done!"


def response_error():
    print(error_prefix, error_response)


def page_success(pageNumber):
    print(success_prefix, scraping_page_start, str(pageNumber), scraping_page_end)


def finished_success():
    print(success_prefix, done)


def success_links():
    print(success_prefix, links)