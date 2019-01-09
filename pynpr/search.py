from algoliasearch import algoliasearch


def search_all(query):
    client = algoliasearch.Client("1SS7XPOA8X",
                                  '9375902912f6f82964c8ec269234b3c2')
    index = client.init_index('nprorg')
    res = index.search(query,
                       {'hitsPerPage': 10}
                       )
    # for audio-only search, add 'hasAudio:true', to filters above.
    # storyIDs = [i['objectID'] for i in res['hits']]
    try:
        return res['hits']
    except:
        return res


def search_podcasts(query):
    for res in search_all(query):
        try:
            yield {"summary": res["teaser"],
                   "episodes": res.get("episodes", []),
                   "podcast": res["podcast"],
                   "date": res["displayDate"]["longDate"],
                   "type": res["type"],
                   "title": res["title"],
                   "url": res["url"]
                   }
        except:
            # not a podcast
            pass


if __name__ == "__main__":
    from pprint import pprint

    pprint(search_all("science")[0])
