import requests
from . import BaseExtractor

# ys-detail-content


class YeniSafak(BaseExtractor):
    def graphql(self, *, url, body):
        r = requests.post(url, json={"query": body})
        # return r.json()
        print("response status code: ", r.status_code)
        if r.status_code == 200:
            print("response : ", r.content)


# 5050
