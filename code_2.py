import pickle
import nltk
import csv
import os, fnmatch

f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

mails=[]
mail ='debit'

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

print (classifier.classify(extract_features(mail.split())))
