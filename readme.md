# PyNPR

Get data from [NPR](https://www.npr.org), info is retrieving by webscrapping and rss feed parsing

WIP - interaction with the npr api is a work in progress for more functionality

# install

    pip install pynpr
    
# usage

check the [examples](./examples)

## browsing npr

    from pynpr import NRPBrowser
    
    NPR = NRPBrowser()
    
    for p in NPR.podcast_categories():
        print(p.name, p.url)
        
    # sample output
    # technology https://www.npr.org/podcasts/2061/technology
    
    for p in NPR.get_featured_podcasts():
        print(p.name, p.url)
        
    # sample output
    # planet money https://www.npr.org/podcasts/510289/planet-money
    
    for show in NPR.get_shows():
        print(show.name, show.url, show.show_type)
        
    # sample output
    # YR Media https://www.npr.org/series/4692815/yr-media series
    # Ask Me Another https://www.npr.org/programs/ask-me-another/ program
    # The Best of Car Talk https://www.npr.org/podcasts/510208/car-talk podcast
    
## searching podcast categories

    from pynpr.podcasts import NPRPodcastCategory

    science = NPRPodcastCategory("https://www.npr.org/podcasts/2047/science-medicine")
    for p in science.podcasts:
        print(p.name, p.url)
    
    # sample output
    # the big one your survival guide https://www.npr.org/podcasts/674580962/the-big-one-your-survival-guide
    # sci show tangents https://www.npr.org/podcasts/664422435/sci-show-tangents
    
## getting podcast info


    from pynpr.podcasts import NPRPodcast
    
    p = NPRPodcast("https://www.npr.org/podcasts/510289/planet-money")
    
    print(p.parse_page())

    # sample output
    # {'Apple Podcasts': 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?s=143441&mt=2&id=290783428&at=11l79Y&ct=nprdirectory',
    #  'Google Podcasts': 'https://www.google.com/podcasts?feed=aHR0cHM6Ly93d3cubnByLm9yZy9yc3MvcG9kY2FzdC5waHA_aWQ9NTEwMjg5',
    #  'NPR One': 'https://rpb3r.app.goo.gl/M4f5',
    #  'Pocket Casts': 'https://pca.st/9NRE',
    #  'RSS link': 'https://www.npr.org/templates/rss/podcast.php?id=510289',
    #  'Spotify': 'https://open.spotify.com/show/4FYpq3lSeQMAhqNI81O0Cn',
    #  'name': 'Planet Money',
    #  'recent_episodes': [],
    #  'related_podcasts': {"Find Money You Didn't Know You Had": 'https://www.npr.org/podcasts/510331/find-money-you-didnt-know-you-had',
    #                       'Full Disclosure with Roben Farzad': 'https://www.npr.org/podcasts/682205174/full-disclosure-with-roben-farzad',
    #                       'Secrets Of Saving And Investing': 'https://www.npr.org/podcasts/510330/secrets-of-saving-and-investing',
    #                       'The Credits': 'https://www.npr.org/podcasts/666151782/the-credits'},
    #  'summary': 'The economy explained. Imagine you could call up a friend and '
    #             'say, "Meet me at the bar and tell me what\'s going on with the '
    #             'economy." Now imagine that\'s actually a fun evening.',
    #  'url': 'https://www.npr.org/planetmoney'}
    
## podcast streams

    from pynpr.podcasts import NPRPodcast
    
    p = NPRPodcast("https://www.npr.org/podcasts/510289/planet-money")
    for stream in p.streams:
        pprint(stream.as_json())
    
    # sample output
    # {'author': 'NPR',
    # 'published': 'Fri, 04 Jan 2019 18:23:00 -0500',
    # 'rights': 'Copyright 2015-2018 NPR - For Personal Use Only',
    # 'streams': ['https://play.podtrac.com/npr-510289/npr.mc.tritondigital.com/NPR_510289/media/anon.npr-podcasts/podcast/npr/pmoney/2019/01/20190104_pmoney_pmpod886-50ee597e-091e-4e23-9c5f-fd6c6c0d13e3.mp3?orgId=1&d=1018&p=510289&story=682331111&t=podcast&e=682331111&ft=pod&f=510289'],
    # 'summary': 'Hackers are an expensive headache for companies. But there might '
    #            'be a simple economic fix.',
    # 'title': '#886: The Price of a Hack'} 
    
## searching NPR

    from pynpr.search import search_podcasts
    from pynpr.podcasts import NPRPodcast
    
    for result in search_podcasts("science"):
        print(result)
        podcast = NPRPodcast(result["url"])
        
    # sample output
    # {'date': 'January 9, 2019',
    #  'episodes': [{'audio': {'duration': 90,
    #                          'id': 683412944,
    #                          'restricted': 'Global'},
    #                'displayDate': {'dateTime': '2019-01-09T03:00:00-05:00',
    #                                'longDate': 'January 9, 2019'},
    #                'hasAudio': True,
    #                'hasImage': False,
    #                'id': 683412942,
    #                'image': {},
    #                'isExplicit': False,
    #                'lastModifiedDate': 1546992000,
    #                'title': 'Stronger Than Silk'},
    #       (....) 
    #               ],
    #  'podcast': {'id': 381444663,
    #              'image': 'https://media-s1.npr.org/images/podcasts/primary/icon_381444663-5a32d6e699f10721710daeccedb4c684e490beb3.jpg',
    #              'name': 'The Loh Down on Science',
    #              'owner': 'KPCC',
    #              'url': 'https://www.scpr.org/programs/loh-down-on-science'},
    #  'summary': 'Hosted by Sandra Tsing Loh, The Loh Down on Science is a fun way '
    #             'to get your daily dose of science plus a dash of humor in less '
    #             'than two minutes.',
    #  'title': 'The Loh Down on Science',
    #  'type': 'podcast',
    #  'url': '/podcasts/381444663/the-loh-down-on-science'}
    
