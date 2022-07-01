import re
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
import requests


def extract_by_class(
    *,
    url: str,
    section: str,
    cls_value: str,
) -> list:
    page = requests.get(url)
    bs = Soup(page.content, "html.parser")
    l = bs.find_all(
        section,
        attrs={
            "class": cls_value,
        },
    )

    return l


# def extract_by_id(*, url: str, section: str, id_value) -> list:
#     page = requests.get(url)
#     bs = Soup(page.content, "html.parser")
#     l = bs.find_all(
#         section,
#         attrs={
#             "id": id_value,
#         },
#     )
#     return l
