# PyNPR

WIP 

# usage


parsing a podcast page

    from pprint import pprint
    
    p = NPRPodcast("https://www.npr.org/podcasts/510289/planet-money")
    pprint(p.parse_page())

output

    {'Apple Podcasts': 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?s=143441&mt=2&id=290783428&at=11l79Y&ct=nprdirectory',
     'Google Podcasts': 'https://www.google.com/podcasts?feed=aHR0cHM6Ly93d3cubnByLm9yZy9yc3MvcG9kY2FzdC5waHA_aWQ9NTEwMjg5',
     'NPR One': 'https://rpb3r.app.goo.gl/M4f5',
     'Pocket Casts': 'https://pca.st/9NRE',
     'RSS link': 'https://www.npr.org/templates/rss/podcast.php?id=510289',
     'Spotify': 'https://open.spotify.com/show/4FYpq3lSeQMAhqNI81O0Cn',
     'name': 'Planet Money',
     'recent_episodes': [{'date': 'January 4, 2019',
                          'teaser': '\n'
                                    'January 4, 2019 • Hackers are an expensive '
                                    'headache for companies. But there might be a '
                                    'simple economic fix.\n'
                                    '        ',
                          'title': '#886: The Price of a Hack'},
                         {'date': 'January 2, 2019',
                          'teaser': '\n'
                                    'January 2, 2019 • People are the engine that '
                                    'fuels an economy. But what happens when you '
                                    'start running out of people?\n'
                                    '        ',
                          'title': '#885: Do It For Your Country'},
                         {'date': 'December 28, 2018',
                          'teaser': '\n'
                                    'December 28, 2018 • We check in on some '
                                    "stories we did this year to see what's "
                                    'changed. Find a full list of the episodes we '
                                    'referenced at our website, NPR.org/money.\n'
                                    '        ',
                          'title': '#884: The Rest Of The Story, Winter 2018'},
                         {'date': 'December 26, 2018',
                          'teaser': '\n'
                                    'December 26, 2018 • How the card game "Magic: '
                                    'The Gathering" deflated a speculative bubble. '
                                    'You can support our show at '
                                    'donate.npr.org/planetmoney.\n'
                                    '        ',
                          'title': '#609: The Curse Of The Black Lotus'},
                         {'date': 'December 24, 2018',
                          'teaser': '\n'
                                    'December 24, 2018 • Most products in this '
                                    'world are vulnerable to creative destruction: '
                                    'as new products are developed, they make old '
                                    'ones obsolete. But there are some exceptions '
                                    '— products that persist, resisting change '
                                    'while economic evolution continues without '
                                    'them. For instance: the graphing calculator. '
                                    '(This episode is from our other podcast, The '
                                    'Indicator from Planet Money. Subscribe to it '
                                    'wherever you get your podcasts.)\n'
                                    '        ',
                          'title': 'BONUS INDICATOR: The Calculator That Time '
                                   'Forgot'},
                         {'date': 'December 21, 2018',
                          'teaser': '\n'
                                    'December 21, 2018 • Charles Dickens wanted to '
                                    'pick a fight with economists. So he invented '
                                    'Ebenezer Scrooge. But did he get it all '
                                    'right? Also: If you want to support our show, '
                                    'head over to donate.npr.org/planetmoney. We '
                                    'appreciate it.\n'
                                    '        ',
                          'title': '#883: A Very Planet Money Christmas Carol'},
                         {'date': 'December 19, 2018',
                          'teaser': '\n'
                                    'December 19, 2018 • How a professor invented '
                                    'a formula for synthesizing cannabinoids and '
                                    'unintentionally helped launch a drug '
                                    'revolution.\n'
                                    '        ',
                          'title': '#882: Synthetic Reefer Madness'},
                         {'date': 'December 17, 2018',
                          'teaser': '\n'
                                    'December 17, 2018 • Ricardo Hausmann, a '
                                    'Harvard-based Venezuelan economist, has '
                                    'constructed his own indicator, one that '
                                    'captures the horrifying scale of the economic '
                                    'catastrophe in Venezuela. (This episode is '
                                    'from our other podcast, The Indicator. '
                                    'Subscribe to it wherever you get your '
                                    'podcasts.)\n'
                                    '        ',
                          'title': 'BONUS INDICATOR: The Measure Of A Tragedy'},
                         {'date': 'December 14, 2018',
                          'teaser': '\n'
                                    'December 14, 2018 • A truce in the U.S.-China '
                                    'trade war seemed close. The leaders of China '
                                    'and the United States were meeting to discuss '
                                    'a fix. And then arrests started. It got even '
                                    'more confusing, so today, we call up our man '
                                    'on the ground in Shanghai to make sense of it '
                                    'all. The key to understanding the latest turn '
                                    'in the trade war centers around a giant '
                                    "company most Americans haven't heard of "
                                    'called Huawei. Its rise traces the rise of '
                                    "China's economy and Chinese-style "
                                    'capitalism.\n'
                                    '        ',
                          'title': '#881: The Prisoners of the Trade War'},
                         {'date': 'December 12, 2018',
                          'teaser': '\n'
                                    'December 12, 2018 • We try to figure out what '
                                    'makes cents.\n'
                                    '        ',
                          'title': "#539: What's A Penny Worth?"}],
     'related_podcasts': {"Find Money You Didn't Know You Had": 'https://www.npr.org/podcasts/510331/find-money-you-didnt-know-you-had',
                          'Full Disclosure with Roben Farzad': 'https://www.npr.org/podcasts/682205174/full-disclosure-with-roben-farzad',
                          'Secrets Of Saving And Investing': 'https://www.npr.org/podcasts/510330/secrets-of-saving-and-investing',
                          'The Credits': 'https://www.npr.org/podcasts/666151782/the-credits'},
     'summary': 'The economy explained. Imagine you could call up a friend and '
                'say, "Meet me at the bar and tell me what\'s going on with the '
                'economy." Now imagine that\'s actually a fun evening.',
     'url': 'https://www.npr.org/planetmoney'}
 
getting podcast categories

    NPR = NRPBrowser()
    for p in NPR.podcast_categories():
        print(p.name, p.url)
        print(p.name)

output

    arts https://www.npr.org/podcasts/2000/arts
    business https://www.npr.org/podcasts/2007/business
    comedy https://www.npr.org/podcasts/2013/comedy
    education https://www.npr.org/podcasts/2014/education
    games hobbies https://www.npr.org/podcasts/2020/games-hobbies
    government organizations https://www.npr.org/podcasts/2026/government-organizations
    health https://www.npr.org/podcasts/2031/health
    kids family https://www.npr.org/podcasts/2036/kids-family
    music https://www.npr.org/podcasts/2037/music
    news politics https://www.npr.org/podcasts/2038/news-politics
    religion spirituality https://www.npr.org/podcasts/2039/religion-spirituality
    science medicine https://www.npr.org/podcasts/2047/science-medicine
    society culture https://www.npr.org/podcasts/2051/society-culture
    sports recreation https://www.npr.org/podcasts/2056/sports-recreation
    technology https://www.npr.org/podcasts/2061/technology
    tv film https://www.npr.org/podcasts/2066/tv-film


getting featured podcasts

    for p in NPR.get_featured_podcast_list():
        print(p.name, p.url)

output

    planet money https://www.npr.org/podcasts/510289/planet-money
    how i built this https://www.npr.org/podcasts/510313/how-i-built-this
    up first https://www.npr.org/podcasts/510318/up-first
    wait wait don t tell me https://www.npr.org/podcasts/344098539/wait-wait-don-t-tell-me
    hidden brain https://www.npr.org/podcasts/510308/hidden-brain
    ted radio hour https://www.npr.org/podcasts/510298/ted-radio-hour
    fresh air https://www.npr.org/podcasts/381444908/fresh-air
    npr politics podcast https://www.npr.org/podcasts/510310/npr-politics-podcast
    tiny desk concerts audio https://www.npr.org/podcasts/510306/tiny-desk-concerts-audio
    the indicator from planet money https://www.npr.org/podcasts/510325/the-indicator-from-planet-money
    1a https://www.npr.org/podcasts/510316/1a
    pop culture happy hour https://www.npr.org/podcasts/510282/pop-culture-happy-hour
    piano jazz shorts https://www.npr.org/podcasts/510056/piano-jazz-shorts
    world cafe words and music from wxpn https://www.npr.org/podcasts/510008/world-cafe-words-and-music-from-wxpn
    bullseye https://www.npr.org/podcasts/510309/bullseye
    only a game https://www.npr.org/podcasts/510052/only-a-game
    here x26 now https://www.npr.org/podcasts/510051/here-x26-now
    from the top https://www.npr.org/podcasts/510026/from-the-top
    car talk https://www.npr.org/podcasts/510208/car-talk
    secrets of saving and investing https://www.npr.org/podcasts/510330/secrets-of-saving-and-investing
    learn to love exercising https://www.npr.org/podcasts/510329/learn-to-love-exercising
    find money you didnt know you had https://www.npr.org/podcasts/510331/find-money-you-didnt-know-you-had
    eat your way to a healthier life https://www.npr.org/podcasts/510328/eat-your-way-to-a-healthier-life
    the indicator from planet money https://www.npr.org/podcasts/510325/the-indicator-from-planet-money
    science medicine https://www.npr.org/podcasts/2047/science-medicine
    wow in the world https://www.npr.org/podcasts/510321/wow-in-the-world
    believed https://www.npr.org/podcasts/510326/believed
    1a https://www.npr.org/podcasts/510316/1a
    fresh air https://www.npr.org/podcasts/381444908/fresh-air
    environment https://www.npr.org/podcasts/381444903/environment
    npr politics podcast https://www.npr.org/podcasts/510310/npr-politics-podcast
    how i built this https://www.npr.org/podcasts/510313/how-i-built-this
    radio ambulante https://www.npr.org/podcasts/510315/radio-ambulante
    latino usa https://www.npr.org/podcasts/510016/latino-usa
    business story of the day https://www.npr.org/podcasts/381444906/business-story-of-the-day
    story of the day https://www.npr.org/podcasts/381444905/story-of-the-day