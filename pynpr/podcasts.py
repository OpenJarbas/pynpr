import requests
from bs4 import BeautifulSoup


class NPRPodcast(object):
    base_url = "https://www.npr.org"
    rss_base = "https://www.npr.org/templates/rss/podcast.php"

    def __init__(self, url):
        if not url.startswith("http"):
            url = self.base_url + url
        self.url = url

    @property
    def rss_url(self):
        rss_id, name = self.url.replace("https://www.npr.org/podcasts/", "") \
            .split("/")
        return self.rss_base + "?id=" + str(rss_id)

    @property
    def rss_id(self):
        rss_id, name = self.url.replace("https://www.npr.org/podcasts/", "") \
            .split("/")
        return rss_id

    @property
    def name(self):
        rss_id, name = self.url.replace("https://www.npr.org/podcasts/", "") \
            .split("/")
        return name.replace("-", " ").strip()

    def parse_page(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, "html.parser")
        main = soup.find("div", {"class": "detail-overview-content col2"})
        data = {}
        data["name"] = main.find("h1").text
        text = main.find("p")
        data["summary"] = text.text.replace("More from " + data["name"] + " »", "")
        data["url"] = text.find("a")["href"]
        streams = main.find("ul", {"class": "podcast-tools"}).find_all("li")
        for s in streams:
            stream_name = s.text.strip()
            stream_url = s.find("a")["href"]
            data[stream_name] = stream_url
        related = soup.find("section",
                            {"class": "podcast-section related-podcasts"})\
            .find("div", {"class": "related-podcasts-inner"})\
            .find_all("article")
        data["related_podcasts"] = {}
        for r in related:
            title = r.find("h1", {"class": "podcast-title"}).text
            url = r.find("a")["href"]
            data["related_podcasts"][title] = url

        data["recent_episodes"] = []
        recent = soup.find("section",
                           {"class": "podcast-section episode-list"})\
            .find_all("article")
        for r in recent:
            try:
                date = r.find("span", {"class": "date"}).text
                title = r.find("h2").text
                teaser = r.find("p", {"class": "teaser"}).text
                data["recent_episodes"].append({"title": title, "date": date,
                                                "teaser": teaser})
            except:
                # load more button
                pass
        return data


class NPRPodcastCategory(object):
    base_url = "https://www.npr.org"
    rss_base = "https://www.npr.org/templates/rss/podcast.php"

    def __init__(self, url):
        if not url.startswith("http"):
            url = self.base_url + url
        self.url = url

    @property
    def category_id(self):
        cat_id, name = self.url.replace("https://www.npr.org/podcasts/", "") \
            .split("/")
        return cat_id

    @property
    def name(self):
        cat_id, name = self.url.replace("https://www.npr.org/podcasts/", "") \
            .split("/")
        return name.replace("-", " ").strip()


class NRPBrowser(object):
    base_url = "https://www.npr.org"

    def podcast_categories(self):
        url = "https://www.npr.org/podcasts/"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        cats = soup.find_all("li", {"class": "subtopics__submenu-item"})
        for c in cats:
            url = c.find("a")["href"]
            yield NPRPodcastCategory(url)

    def get_featured_podcast_list(self, url="/podcasts/"):
        url = "https://www.npr.org" + url
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        next_page = soup.find("a", {"class": "more-podcasts"})
        podcasts = soup.find_all("article", {"class": "item"})
        for p in podcasts:
            url = p.find("a")["href"]
            yield NPRPodcast(url)
        if next_page:
            for p in self.get_featured_podcast_list(next_page["href"]):
                yield p


if __name__ == "__main__":

    from pprint import pprint
    p = NPRPodcast("https://www.npr.org/podcasts/510289/planet-money")
    pprint(p.parse_page())

    NPR = NRPBrowser()
    for p in NPR.podcast_categories():
        print(p.name, p.url)

    for p in NPR.get_featured_podcast_list():
        print(p.name, p.url)
