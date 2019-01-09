from pynpr.podcasts import NPRPodcastCategory

science = NPRPodcastCategory("https://www.npr.org/podcasts/2047/science-medicine")
for p in science.podcasts:
    print(p.name, p.url)