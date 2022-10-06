# Phase 1(a):   Twitter APIs

Phase 1(a) aims to write a program as an exercise to learn the different Twitter API commands available for developers. The second part of Phase 1(a) demonstrates how I used Botometer (a Twitter account activity checker that evaluates whether or not the account is a bot) API calls.

The following are some examples of Twitter's API calls:

## Making a Simple Search Query
```python
query = 'from: elonmusk -is:retweet'
personal_tweets = client.search_recent_tweets(query=query,
                                    tweet_fields=['author_id', 'created_at'],
                                    max_results=10)

tweet_dict = personal_tweets.json()
print(tweet_dict)
```

Output:
```
{'data': [{'edit_history_tweet_ids': ['1578055594573004800'], 'text': 'Starlink view of 2nd stage deorbit burn https://t.co/kbLv95bAK7', 'id': '1578055594573004800', 'author_id': '44196397', 'created_at': '2022-10-06T16:12:27.000Z'}, {'edit_history_tweet_ids': ['1578050963889393664'], 'text': '@realAdrianDa32 @HuXijin_GT 👍🤣', 'id': '1578050963889393664', 'author_id': '44196397', 'created_at': '2022-10-06T15:54:03.000Z'}, {'edit_history_tweet_ids': ['1578049022102851584'], 'text': '@HuXijin_GT 手整体插在口袋里 'id': '1578049022102851584', 'author_id': '44196397', 'created_at': '2022-10-06T15:46:20.000Z'}, {'edit_history_tweet_ids': ['1578046964087898113'], 'text': '@Xu0P5C4rMmMKUdu @stillgray @atrupar @LindseyGrahamSC I will try my best', 'id': '1578046964087898113', 'author_id': '44196397', 'created_at': '2022-10-06T15:38:09.000Z'}, {'edit_history_tweet_ids': ['1578041621093949440'], 'text': '@KyivPost I’m a big fan of Ukraine, but not of WW3', 'id': '1578041621093949440', 'author_id': '44196397', 'created_at': '2022-10-06T15:16:55.000Z'}, {'edit_history_tweet_ids': ['1578025984003305475'], 'text': '@spideycyp_155 @garyblack00 🤣', 'id': '1578025984003305475', 'author_id': '44196397', 'created_at': '2022-10-06T14:14:47.000Z'}, {'edit_history_tweet_ids': ['1578021743532208129'], 'text': '@garyblack00 https://t.co/FxgYMhTax6', 'id': '1578021743532208129', 'author_id': '44196397', 'created_at': '2022-10-06T13:57:56.000Z'}, {'edit_history_tweet_ids': ['1578020826674184193'], 'text': '@Rainmaker1973 Cute. You can get surprisingly close to a wild baby rhino &amp; Mom if you stay downwind.', 'id': '1578020826674184193', 'author_id': '44196397', 'created_at': '2022-10-06T13:54:17.000Z'}, {'edit_history_tweet_ids': ['1578002979927515137'], 'text': '@stillgray @atrupar @LindseyGrahamSC There are no angels in war.', 'id': '1578002979927515137', 'author_id': '44196397', 'created_at': '2022-10-06T12:43:22.000Z'}, {'edit_history_tweet_ids': ['1577894684109717510'], 'text': '@EliClifton @DavidSacks Accurate assessment', 'id': '1577894684109717510', 'author_id': '44196397', 'created_at': '2022-10-06T05:33:03.000Z'}], 'meta': {'newest_id': '1578055594573004800', 'oldest_id': '1577894684109717510', 'result_count': 10, 'next_token': 'b26v89c19zqg8o3fpzbmmev2eewdb4xjukfmwoit2h6d9'}}

```
## Making a Query Search Based on Specified Dates
```python
query = "#covid19 lang:en -is:retweet"
start_time = "2022-09-30T00:00:00Z"
end_time = "2022-10-01T00:00:00Z"

tweets = client.search_recent_tweets(query=query,
                                     start_time=start_time,
                                     end_time=end_time,
                                     tweet_fields = ["created_at", "text", "source"],
                                     user_fields = ["name", "username", "location", "verified", "description"],
                                     max_results = 10,
                                     expansions='author_id'
                                     )
tweets_dict = tweets.json()
print(tweets_dict)
```
Output:
```
{'data': [{'edit_history_tweet_ids': ['1575998730435973121'], 'author_id': '47798160', 'id': '1575998730435973121', 'created_at': '2022-09-30T23:59:12.000Z', 'source': 'Twitter Web App', 'text': '@JenniferSey That is truly pathetic. My parents were actually hit extremely hard. There house started to flood. The last thing on any of our minds was #covid19.'}, {'edit_history_tweet_ids': ['1575998448100593664'], 'author_id': '118788479', 'id': '1575998448100593664', 'created_at': '2022-09-30T23:58:05.000Z', 'source': 'Twitter Web App', 'text': 'September 30, 2022. Nationwide Wastewater Monitoring Network shows #COVID19 trends in communities across the US.  #data #analytics #wastewater #epidemiology https://t.co/soitAQM2EI\nHmm, a slight climb here... https://t.co/KVJM7iwWqt'}, {'edit_history_tweet_ids': ['1575998311877603329'], 'author_id': '824014804016893953', 'id': '1575998311877603329', 'created_at': '2022-09-30T23:57:32.000Z', 'source': 'Twitter Web App', 'text': 'Every week, just as many people die of #Covid19 as did during the horrific 9/11 attacks. EVERY WEEK! Think about that.'}, {'edit_history_tweet_ids': ['1575998213676417024'], 'author_id': '154266844', 'id': '1575998213676417024', 'created_at': '2022-09-30T23:57:09.000Z', 'source': 'Twitter Web App', 'text': '#health LINKS TO CORONAVIRUS AND HEALTH 2022 #battling_coronavirus #Biden_administration #coronavirus #sickness #covid19 #illness #COVID_hospitalizations #vaccine_mandates #anti_vaccine #anti_vaxxers\nhttps://t.co/G7x7o3uzcX\nhttps://t.co/SB8PN5585f'}, {'edit_history_tweet_ids': ['1575998003172691968'], 'author_id': '928758157672722433', 'id': '1575998003172691968', 'created_at': '2022-09-30T23:56:19.000Z', 'source': 'Twitter Web App', 'text': 'This Hurricane Is Leaving The Supply Chain In A Wreck.\nhttps://t.co/uIR4nXnVec\n\n#hurricaneian #supplychain #federalresponse #COVID19 #Category4\n\nFollow Us!\nPinterest: #safelineinsurance\nFacebook: https://t.co/uJEcRjiwlM https://t.co/DX0fX4vrQj'}, {'edit_history_tweet_ids': ['1575997986072539136'], 'author_id': '1263418475961171979', 'id': '1575997986072539136', 'created_at': '2022-09-30T23:56:15.000Z', 'source': 'Twitter Web App', 'text': '#Singapore seeing a rise in #covid19 cases related to #omicron but no extra demand on health services it seems. #pandemic #travel #business #masks #vaccines #mumbai #hongkong #china #tourism #Formula1 #F1 #SingaporeGP \nhttps://t.co/ksAd0TnUiu'}, {'edit_history_tweet_ids': ['1575997881810444288'], 'author_id': '118788479', 'id': '1575997881810444288', 'created_at': '2022-09-30T23:55:50.000Z', 'source': 'Twitter Web App', 'text': 'September 30, 2022. Nationwide Wastewater Monitoring Network shows #COVID19 trends in communities across the US.  #data #analytics #wastewater #epidemiology https://t.co/cOzYUCGf4Z https://t.co/RaxYMksUes'}, {'edit_history_tweet_ids': ['1575997821529964545'], 'author_id': '1548604523865788418', 'id': '1575997821529964545', 'created_at': '2022-09-30T23:55:35.000Z', 'source': 'Twitter for Android', 'text': "@DataDrivenMD Our friend took the #mRNA jab and died\nIn his 50's\nLeaves behind 2 children and a loving wife\nThanks, but no thanks \nI've had #COVID19 twice and it was a bad flu"}, {'edit_history_tweet_ids': ['1575997560351002624'], 'author_id': '29924184', 'id': '1575997560351002624', 'created_at': '2022-09-30T23:54:33.000Z', 'source': 'Twitter for iPhone', 'text': 'What complete bullshit. “Old age”! Why are they afraid of releasing what she actually died from? \n\nWas it COVID-related? Did she fail to recover from her bout in February?\n\nThe “live with COVID” government wouldn’t want to let that out would it.\n\n#COVID19 #QueenElizabethII https://t.co/MY3V8WAGim'}, {'edit_history_tweet_ids': ['1575997544525545472'], 'author_id': '1016943828052336640', 'id': '1575997544525545472', 'created_at': '2022-09-30T23:54:29.000Z', 'source': 'Twitter Web App', 'text': '3 NSW road deaths prompt police to urge caution over long weekend.\n\nMeanwhile, no caution urged for the dozens who will die from COVID this weekend!\n\n#WearAMask #CovidIsNotOver #CovidIsntOver #COVID19 #Covid19Aus #auspol #LetItRip #insiders'}], 'includes': {'users': [{'name': 'Lesann63', 'description': 'I fight for what I believe in. Love God, Country, and family.  Licensed Clinical Professional Counselor  #gymnastalliance', 'verified': False, 'username': 'mbrave63', 'id': '47798160'}, {'location': 'United States', 'name': 'Betty C. Jung', 'description': 'Betty C. Jung MPH RN MCHES® Adjunct lecturer, Public Health; PHENOM Director; Webmaster #PublicHealth #Health #Science #Technology #Culture #COVID19', 'verified': False, 'username': 'bettycjung', 'id': '118788479'}, {'location': 'In a van DOWN BY THE RIVER', 'name': 'The Lazy Vulcan', 'description': "I am an aggressive non-participant in a society that I don't believe in.\n#Resist\n#NewEnglander\n#Trekkie\n#HockeyFan\n#ProChoice\n#StarWars", 'verified': False, 'username': 'RealLazyVulcan', 'id': '824014804016893953'}, {'location': 'Rural Hall, NC', 'name': 'Tom Gillispie -- NATURE NEEDS OUR HELP 🦮🌎🌊🏈', 'description': '■ NO DMs ★ DEMOCRACY ★ BOOSTED ★ SCIENCE ★ WRITING ★ DOGS (DIXIE) \n★ BASEBALL ★ MIAMI DOLPHINS ★ HUMOR ★ SINGING ★ STAR TREK \n★ MYSTERIES ★ WESTERNS', 'verified': False, 'username': 'SptsGuy1', 'id': '154266844'}, {'name': 'Safeline Truck Insurance', 'description': 'SafeLine Truck Insurance is an insurance agency in Burbank, California. In addition, we are specialized in commercial truck insurance.', 'verified': False, 'username': 'SafelineTruck', 'id': '928758157672722433'}, {'location': 'Asia', 'name': 'Business Mobility Asia', 'description': 'Information for business mobility across Asia during COVID19 Pandemic, updated regularly', 'verified': False, 'username': 'asia_mobility', 'id': '1263418475961171979'}, {'location': 'Melbourne, Victoria', 'name': 'Felicity Electricity', 'description': 'I would rather eat grass on a medium strip that submit myself to any covid non science\nPart of the control group who have functioning braincells', 'verified': False, 'username': 'felicityaus', 'id': '1548604523865788418'}, {'name': 'Neil Brennan 🌊', 'description': 'Nutritionist, alternative practitioner, minister in the Universal Life Church, CTO. And everything else that takes no rigour or training. Just like you. He/Him', 'verified': False, 'username': 'nellophonic', 'id': '29924184'}, {'location': 'Gadigal Land, Eora Nation 🦘', 'name': 'C h r i s 🏳️\u200d🌈 🏳️\u200d⚧️ 🌏 🌲 #VoteYes 🖤💛❤️', 'description': 'Labor & union proud\n#CovidIsNotOver \n#WearAMask  😷\n#IStandWithUkraine🇺🇦 \nLGTBIQ+ 🏳️\u200d🌈 🏳️\u200d⚧️\n#ClimateActionNow ⛈️ \n#MurdochRoyalCommission\nCycle🚴\u200d♂️', 'verified': False, 'username': 'ChrisHeHim1', 'id': '1016943828052336640'}]}, 'meta': {'newest_id': '1575998730435973121', 'oldest_id': '1575997544525545472', 'result_count': 10, 'next_token': 'b26v89c19zqg8o3fpzbls5rwu6ig0samincpvjthj6qgt'}}

```

The following are some examples of Botometer's API calls:

```python
bom = botometer.BotometerLite(rapidapi_key=rapid_api_key,)

result = bom.check_account('@elonmusk')
print(result)

```
Output:
```
tweepy.error.TweepError: [{'message': 'You currently have Essential access which includes access to Twitter API v2 endpoints only. If you need access to this endpoint, you’ll need to apply for Elevated access via the Developer Portal. You can learn more here: https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-leve', 'code': 453}]
```
Unfortunately, Botometer does not currently work with Essential access endpoints. I am working on elevating my user privileges on my Twitter developer account.


# Phase 1(b)
Phase 1(b) of the project is an exercise on google's NLP sentiment analysis APIs.

The following is an example on how I used Google NLP Senitment Analysis.

```python
client = language_v1.LanguageServiceClient()

text_content = 'I am so happy and joyful.'

# Available types: PLAIN_TEXT, HTML
type_ = language_v1.Document.Type.PLAIN_TEXT

# Optional. If not specified, the language is automatically detected.
# For list of supported languages:
# https://cloud.google.com/natural-language/docs/languages
language = "en"
document = {"content": text_content, "type_": type_, "language": language}

# Available values: NONE, UTF8, UTF16, UTF32
encoding_type = language_v1.EncodingType.UTF8

response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
# Get overall sentiment of the input document
print(u"Document sentiment score: {}".format(response.document_sentiment.score))
print(u"Document sentiment magnitude: {}".format(response.document_sentiment.magnitude))
```
Output:
```
Document sentiment score: 0.8999999761581421
Document sentiment magnitude: 0.8999999761581421

```
