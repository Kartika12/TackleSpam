import nltk
import csv

pos_tweets = [
('Loving the weather in Delhi today...Its just amazing!','positive'),
('Awesome weather in delhi. Just got back from a walk','positive'),
('today\'s weather in Delhi reminded me of many great weather places. miss pune (of 15 yrs back), pondicherry and helsinki :|','positive'),
('Really great weather in delhi! Going home with the window rolled down and the hair haywire \m/','positive'),
('Extremely pleasant weather in Delhi temp must 18 or 20c ...','positive'),
('Nice weather in Delhi NCR, and met college friends over movie and lunch. Bliss!','positive'),
('Extremely pleasant weather in Delhi temp must 18 or 20c ...','positive'),
('Lovely weather in Delhi! But BJP under the weather!','positive'),
('amazing weather in delhi, the clouds have finally reached us on this day of the harvest moon.sat in the lawn with the purplesunbird4 company','positive'),
('@dotmanish good morning sweets.:-) nice weather in delhi today','positive'),
('Pleasant weather in Delhi but no rain in store: New Delhi, May 12 : After a pleasant start to the week following.. http://tinyurl.com/q8vpqc','positive'),
('GM! @docrajen Thanks. I love winters & am really loving the weather in Delhi now.I have lived in Ladakh 4 two yrs. I just wither in summers.','positive'),
('News India: Pleasant weather in Delhi: New Delhi, Nov 16 (PTI) Delhiites experienced a pleasant weat.. http://bit.ly/4qCv4z','positive'),
('It\'s great weather in Delhi. Going book shopping.','positive'),
('mornin\' tweeps... great weather in delhi for last couple of days yay!','positive'),
('reached delhi after a long long flight via bombay. bad idea taking d cheaper, longer route. on d bright side,weather in delhi is really gud!','positive'),
('Lovely weather in delhi.. Cool breeze.. Taking a walk outside the house in places whr the wifi is still reachable','positive'),
('Awesome weather in delhi','positive'),
('the weather in Delhi is perfect right now.','positive'),
('Finally great weather in delhi. Onset of winters.:)','positive'),
('Lovely weather in Delhi...heading headlong into winters.','positive'),
('awesome weather in delhi !','positive'),
('Awesome weather in delhi right now. I wanna go home right now. *searches for floo powder*','positive'),
('Yeah... the weather in Delhi late in the nights is stunning! @sarkar_purba','positive'),
('Amazing weather in Delhi... Going out for a cup of coffee','positive'),
('awesome weather in delhi...the winters r finally in...sexy cold winds blowing','positive'),
('wow what a pleasant weather in Delhi','positive'),
('Pleasant weather greets Delhi again Wednesday http://tinyurl.com/mpvca6','positive'),
('Awesome weather in Delhi on a monday morning. Very bad timing!','positive'),
('its an amazing weather in Delhi today. cool breeze,making me feel as if i am at a hill station. :)','positive'),
('The weather in Delhi right now is nothing short of orgasmic.','positive'),
('The weather in delhi is getting awesomer day by day :D Time to take out jackets and hoodies soon! @SakshiKumar','positive'),
('The weather is Delhi has improved so much that the cooler feels like an AC now.','positive'),
('but #mumbai got better now with #rain RT @ReemaKapur: It\'s a good weather in Delhi','positive'),
('Weather in Delhi is cool today :) Enjoying','positive'),
('Lovely weather in Delhi today. For a change did not want to reach the destination. Wish the path never ended.','positive'),
('Lovely weather in Delhi to go out. Had a great time roaming around.','positive'),
('lovely weather in delhi again. Outside, Sipping chai (not tea), dunking biscuits, watching history lessons from iTunes U','positive'),
('Yep. Lovely weather in Delhi region today.','positive'),
('Wonderful weather in Delhi today. Nice & cool, with a slight breeze. Zero humidity. Outside, its much worse though.','positive'),
('Its such a *beautiful* weather in Delhi. BEAUTIFUL!','positive')
]

neg_tweets = [
('bad weather in delhi. Internet dead. Glad i\'m home on time.','negative'),
('Landed safely in terrible weather in Delhi Now stuck in bad jam http://bit.ly/dcYXu http://yfrog.com/ccj02j','negative'),
('So now the flight lands in Nagpur..bad weather in Delhi ....c\'est la vie','negative'),
('Indigo announces delay due to \'bad weather in Delhi.\' Jet announces boarding for Delhi. Simultaneously!','negative'),
('Alright then, Indigo\'s flight to Delhi delayed by 40 min due to \'bad weather in Delhi.\' There goes my meeting.','negative'),
('Flight to Mumbai from Goa delayed cause of bad weather in Delhi. Talk about irony…','negative'),
('Hot and humid weather makes Delhi fret - Delhi woke up to a hot and humid morning Thursday. The weather office has,...http://bit.ly/ciyoZE','negative'),
('Nice to be back to the wet weather here from the hot and humid weather in Delhi!','negative'),
('Don\'t be fooled by clouds in sky. Its the same pathetically hot weather in Delhi even now.','negative'),
('The weather in Delhi has been most unbearable over the past few days. Hot and muggy...','negative'),
('Was a real bumpy last 1 hour of flight. Terible weather in Delhi.plane landed in extreme lightening and rain. Was scary. Thank God landed.','negative'),
('@PritishNandy Never really liked weather\'s of Delhi, Mumbai and Kolkata..everything is way to extreme !!','negative'),
('@Sharanya yeah peach tree. bt the weather in delhi is nt conducive to its growth :\\','negative')
]

tweets = []

#combining the tweets and keeping only words that are longer than 2 letters.

for (words,sentiment) in pos_tweets + neg_tweets:
	words_filtered = [e.lower() for e in words.split() if len(e)>=3]
	tweets.append((words_filtered,sentiment))

#for tweet in tweets:
#	print tweet

def get_words_in_tweets(tweets):
	all_words = []
	for (words,sentiment) in tweets:
		all_words.extend(words)
	return all_words

#getting frequencies of each word

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

word_features = get_word_features(get_words_in_tweets(tweets))


def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)'%word] = (word in document_words)
	return features

training_set = nltk.classify.apply_features(extract_features,tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)


tweet = "weather is nice"
print (classifier.classify(extract_features(tweet.split())))
