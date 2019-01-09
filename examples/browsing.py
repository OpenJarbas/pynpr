from pynpr.podcasts import NRPBrowser

NPR = NRPBrowser()
for p in NPR.podcast_categories():
    print(p.name, p.url)

for p in NPR.get_featured_podcast_list():
    print(p.name, p.url)
