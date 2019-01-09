from pynpr.podcasts import NPRPodcast
from pprint import pprint

p = NPRPodcast("https://www.npr.org/podcasts/510289/planet-money")
pprint(p.parse_page())
