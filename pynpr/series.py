import requests
from bs4 import BeautifulSoup
from pynpr.programs import NPRProgram


class NPRSeries(NPRProgram):

    @property
    def name(self):
        if self._name:
            return self._name
        rss_id, name = self.url.replace("https://www.npr.org/series/", "") \
            .split("/")
        return name.replace("-", " ").strip()

    def parse_page(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, "html.parser")
        data = {}
        # TODO
        return data


