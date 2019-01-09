from pynpr.podcasts import NPRPodcast
from pprint import pprint

p = NPRPodcast("https://www.npr.org/podcasts/510289/planet-money")

for stream in p.streams:
    pprint(stream.as_json())

pprint(p.parse_page())

pprint(p.rss_data)
