import pickle
import nltk
import os, fnmatch


def findFiles(path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)


ham_mails = []
for textFile in findFiles(r'Data/ham', '*.txt'):
    fileobj = open(textFile, 'r')
    for line in fileobj:
        for word in line.split():
            if len(word) > 3:
                ham_mails.append((word, 'positive'))

spam_mails = []
for textFile in findFiles(r'Data/spam', '*.txt'):
    fileobj1 = open(textFile, 'r')
    for line in fileobj1:
        for word in line.split():
            if len(word) > 3:
                spam_mails.append((word, 'negative'))

mails = []

for (words, sentiment) in spam_mails + ham_mails:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    mails.append((words_filtered, sentiment))

def get_words_in_mails(mails):
    all_words = []
    for (words, sentiment) in mails:
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
        features['contains(%s)' % word] = (word in document_words)
    return features

print('a')
# First Trainer to classify into ham and spam
training_set = nltk.classify.apply_features(extract_features, mails)
classifier = nltk.NaiveBayesClassifier.train(training_set)

fileobj2 = open('Data/chk.txt', 'r')
mail = 'offer'

# Stores the pickled object as my_classifier.pickle

print(classifier.classify(extract_features(mail.split())))
f = open('my_classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()
print('b')
print('Done')
