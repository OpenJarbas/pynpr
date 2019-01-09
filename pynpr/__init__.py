import requests
from bs4 import BeautifulSoup
from pynpr.podcasts import NPRPodcast, NPRPodcastCategory
from pynpr.programs import NPRProgram, ExternalNPRProgram
from pynpr.series import NPRSeries
from pynpr.sections import NPRSection


class NRPBrowser(object):
    base_url = "https://www.npr.org"

    def podcast_categories(self):
        url = self.base_url + "/podcasts/"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        cats = soup.find_all("li", {"class": "subtopics__submenu-item"})
        for c in cats:
            url = c.find("a")["href"]
            yield NPRPodcastCategory(url)

    def get_featured_podcasts(self, url="/podcasts/"):
        url = self.base_url + url
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        next_page = soup.find("a", {"class": "more-podcasts"})
        podcasts = soup.find_all("article", {"class": "item"})
        for p in podcasts:
            url = p.find("a")["href"]
            yield NPRPodcast(url)
        if next_page:
            for p in self.get_featured_podcasts(next_page["href"]):
                yield p

    def get_shows(self):
        url = self.base_url + "/programs/"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        sections = soup.find_all("section", {"class": "program-section"})
        for s in sections:
            programs = s.find_all("article")
            for p in programs:
                title = p.find("h3").text
                url = p.find("a")["href"]
                if "/podcasts/" in url:
                    yield NPRPodcast(url, title)
                elif "/programs/" in url:
                    yield NPRProgram(url, title)
                elif "/series/" in url:
                    yield NPRSeries(url, title)
                elif "/sections/" in url:
                    yield NPRSection(url, title)
                else:
                    yield ExternalNPRProgram(url, title)


if __name__ == "__main__":

    NPR = NRPBrowser()
    for show in NPR.get_shows():
        print(show.name, show.url)
