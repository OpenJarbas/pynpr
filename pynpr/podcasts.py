import requests
from bs4 import BeautifulSoup
from pynpr.programs import NPRProgram


class NPRPodcast(NPRProgram):
    rss_base = "https://www.npr.org/templates/rss/podcast.php"

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
        if self._name:
            return self._name
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
        data["summary"] = text.text.replace("More from " + data["name"] + " »",
                                            "")
        data["url"] = text.find("a")["href"]
        streams = main.find("ul", {"class": "podcast-tools"}).find_all("li")
        for s in streams:
            stream_name = s.text.strip()
            stream_url = s.find("a")["href"]
            data[stream_name] = stream_url
        related = soup.find("section",
                            {"class": "podcast-section related-podcasts"}) \
            .find("div", {"class": "related-podcasts-inner"}) \
            .find_all("article")
        data["related_podcasts"] = {}
        for r in related:
            title = r.find("h1", {"class": "podcast-title"}).text
            url = r.find("a")["href"]
            data["related_podcasts"][title] = url

        data["recent_episodes"] = []
        recent = soup.find("section",
                           {"class": "podcast-section episode-list"}) \
            .find_all("article")
        for r in recent:
            try:
                date = r.find("span", {"class": "date"}).text.strip()
                num, title = r.find("h2").text.split(":")
                teaser = r.find("p", {"class": "teaser"}).text.strip()
                data["recent_episodes"].append(
                    {"title": title.strip(),
                     "date": date,
                     "episode_number": num.replace("#").strip(),
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

    @property
    def podcasts(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, "html.parser")
        main = soup.find("section", {"class": "podcast-section"})
        podcasts = main.find_all("article", {"class": "item"})[1:]
        for p in podcasts:
            url = p.find("a")["href"]
            if url:
                yield NPRPodcast(url)


if __name__ == "__main__":
    from pprint import pprint

    p = NPRPodcast("https://www.npr.org/podcasts/510289/planet-money")
    pprint(p.parse_page())
