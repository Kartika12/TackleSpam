
import nltk
import csv
import os, fnmatch


def findFiles(path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)


ham_mails = []
for textFile in findFiles(r'Data/ham', '*.txt'):
    print(textFile)
    for line in textFile:
        for word in line.split():
            ham_mails.append((word, 'positive'))
print(ham_mails)

print('spam starts here')
spam_mails = []
for textFile in findFiles(r'Data/spam', '*.txt'):
    print(textFile)
    for line in textFile:
        for word in line.split():
            spam_mails.append((word, 'negative'))
print(spam_mails)

# spam_mails = [
# ('Lucky Draw win','negative'),
# ('Lottery','negative'),
# ('million dollars','negative'),
# ('gold','negative')]

# ham_mails = [('meeting','positive'),
# ('lunch','positive'),
# ('how are you','positive')
# ]

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


training_set = nltk.classify.apply_features(extract_features, mails)

classifier = nltk.NaiveBayesClassifier.train(training_set)

# fileobj2 = open('Data/chk.txt','r')
mail = 'hello'
print(classifier.classify(extract_features(mail.split())))
