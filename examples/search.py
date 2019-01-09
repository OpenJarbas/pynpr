from pynpr.search import search_podcasts
from pynpr.podcasts import NPRPodcast

from pprint import pprint

for result in search_podcasts("science"):
    pprint(result)
    podcast = NPRPodcast(result["url"])
    for stream in podcast.streams:
        pprint(stream.as_json())

    pprint(podcast.parse_page())
