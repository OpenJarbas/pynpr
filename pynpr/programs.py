import requests
from bs4 import BeautifulSoup


class NPRProgram(object):
    base_url = "https://www.npr.org"

    def __init__(self, url, name=""):
        self._name = name
        if not url.startswith("http"):
            url = self.base_url + url
        self.url = url

    @property
    def name(self):
        if self._name:
            return self._name
        rss_id, name = self.url.replace("https://www.npr.org/programs/", "") \
            .split("/")
        return name.replace("-", " ").strip()

    def parse_page(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, "html.parser")
        data = {}
        # TODO
        return data


class ExternalNPRProgram(NPRProgram):
    def __init__(self, url, name=""):
        NPRProgram.__init__(self, url, name)
        self.base_url = url


