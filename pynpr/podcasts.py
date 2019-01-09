import requests
from bs4 import BeautifulSoup
import feedparser
import json
from pynpr.programs import NPRProgram


class NPRStream(object):
    def __init__(self, author="NPR", summary="", title="", streams=None):
        self.author = author
        self.summary = summary
        self.title = title
        self.streams = streams or []
        self.rights = 'Copyright 2015-2018 NPR - For Personal Use Only'
        self.published = ""

    def from_data(self, data):
        if isinstance(data, str):
            data = json.loads(data)
        self.author = data.get("author", self.author)
        self.summary = data.get("summary", self.summary)
        self.title = data.get("title", self.title)
        self.rights = data.get("rights", self.rights)
        links = data.get("links", [])
        for l in links:
            if l["type"] == "audio/mpeg":
                self.streams.append(l["href"])
        self.published = data.get("published", self.published)
        return self

    def as_json(self):
        return {"author": self.author, "published": self.published,
                "summary": self.summary, "streams": self.streams,
                "title": self.title, "rights": self.rights}



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
    def rss_data(self):
        return feedparser.parse(self.rss_url)

    @property
    def streams(self):
        return [NPRStream().from_data(e) for e in self.rss_data.entries]

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
        data = {"url": self.url}
        data["name"] = main.find("h1").text
        text = main.find("p")
        data["summary"] = text.text.replace("More from " + data["name"] + " »",
                                            "")
        url = text.find("a")
        if url:
            data["url"] = url["href"]
        streams = main.find("ul", {"class": "podcast-tools"}).find_all("li")
        for s in streams:
            stream_name = s.text.strip()
            stream_url = s.find("a")["href"]
            data[stream_name] = stream_url

        data["related_podcasts"] = {}
        try:
            related = soup.find("section",
                                {"class": "podcast-section related-podcasts"}) \
                .find("div", {"class": "related-podcasts-inner"}) \
                .find_all("article")

            for r in related:
                try:
                    title = r.find("h1", {"class": "podcast-title"}).text
                    url = r.find("a")["href"]
                    data["related_podcasts"][title] = url
                except:
                    # just in case
                    pass
        except:
            # some search results fail, TODO find out why
            pass
        data["recent_episodes"] = []

        try:
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
        except:
            # just in case
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
    for s in p.streams:
        pprint(s.as_json())