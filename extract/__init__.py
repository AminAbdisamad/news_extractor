import re
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
import requests
from urllib.request import urlopen


# How to create a class in python
class BaseExtractor:
    # A class can have one more more methods
    # A method is a function inside a class
    # Fuction is a block of related code
    def find(self, *, url: str, section: str, value: str):
        """Find takes three arguments (url, section,value)
        and returns a list of elements found

        @notes: please keep in mind that this method uses
        the requests library to make a request to the url
        """
        page = requests.get(
            url,
        )

        bs = Soup(page.content, "html.parser")
        l = bs.find_all(
            section,
            attrs={
                "class": value,
            },
        )
        return l

    def find_with_urlopen(self, *, url: str, section: str, value: str):
        """Find takes three arguments (url, section,value)
        and returns a list of elements found

        @notes: please keep in mind that this method uses
        the requests library to make a request to the url
        """

        with urlopen(url, timeout=1) as web:
            page = web.read()

            bs = Soup(page, "html.parser")
            l = bs.find_all(
                section,
                attrs={
                    "class": value,
                },
            )
            return l

    def clean_text(self, text):
        """@description: clean the data

        @return: cleaned data
        """
        symbols = ["(", ")", ".", ",", "\u2014", "\u2019s", "\u25a0"]
        for symbol in symbols:
            text = text.replace(symbol, "")
        return text

    def graphql(self, *, url: str, body: str) -> tuple[int, dict]:
        r = requests.post(url, json={"query": body})
        return (r.status_code, r.json())
