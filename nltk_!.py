import nltk
import csv

spam_mails = [
('Lucky Draw win','negative'),
('Lottery','negative'),
('million dollars','negative'),
('gold','negative'),
('million dollars','negative')
]

ham_mails = [('meeting','positive'),
('lunch','positive'),
('how are you','positive')
]

mails = []

for (words,sentiment) in spam_mails + ham_mails:
	words_filtered = [e.lower() for e in words.split() if len(e)>=3]
	mails.append((words_filtered,sentiment))



def get_words_in_mails(mails):
	all_words = []
	for (words,sentiment) in mails:
		all_words.extend(words)
	return all_words



def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

word_features = get_word_features(get_words_in_mails(mails))


def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)'%word] = (word in document_words)
	return features

training_set = nltk.classify.apply_features(extract_features,mails)

classifier = nltk.NaiveBayesClassifier.train(training_set)


mail = "meeting"
print (classifier.classify(extract_features(mail.split())))
