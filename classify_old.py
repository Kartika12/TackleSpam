import pickle
import nltk
import csv
import os, fnmatch

f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)



mails=[]
#fileobj2=open('Data/chk2.txt','r')
#mail =fileobj2.read()

mail = 'nigeria'
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)


advertisment_mails=[]
for textFile in findFiles(r'Data/advertisment', '*.txt'):
    fileobj=open(textFile,'r')
    for line in fileobj:
        for word in line.split():
            if len(word)>3:
                advertisment_mails.append((word,'advertisment'))
print('Advertisment_Mails')
print(advertisment_mails)

forgery_mails=[]
for textFile in findFiles(r'Data/forgery','*.txt'):
   fileobj1=open(textFile,'r')
   for line in fileobj1:
      for word in line.split():
         if len(word)>3:
            forgery_mails.append((word,'forgery'))
print('Forgery_Mails')
print(forgery_mails)

lottery_mails=[]
for textFile in findFiles(r'Data/lottery','*.txt'):
   fileobj1=open(textFile,'r')
   for line in fileobj1:
      for word in line.split():
         if len(word)>3:
            lottery_mails.append((word,'lottery'))

print('Lottery_Mails')
print(lottery_mails)


for (words,sentiment) in advertisment_mails + forgery_mails + lottery_mails:
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
   features=document
   document_words = set(document)
   features = {}
   for word in word_features:
      features['contains(%s)'%word] = (word in document_words)
   return features

print (classifier.classify(extract_features(mail.split())))
f.close()
