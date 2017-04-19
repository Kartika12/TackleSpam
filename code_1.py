import pickle
import nltk
import csv
import os, fnmatch

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

#CHANGED CODE STARTS HERE
mails=[]
advertisment_mails=[]
for textFile in findFiles(r'Data/advertisment', '*.txt'):
    fileobj=open(textFile,'r')
    for line in fileobj:
        for word in line.split():
            if len(word)>3:
                advertisment_mails.append((word,'Advertisment'))
print('Advertisment_Mails')
print(advertisment_mails)

forgery_mails=[]
for textFile in findFiles(r'Data/forgery','*.txt'):
   fileobj1=open(textFile,'r')
   for line in fileobj1:
      for word in line.split():
         if len(word)>3:
            forgery_mails.append((word,'Forgery/Lottery'))
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
# CHANGED CODE ENDS HERE

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


#fileobj2 = open('Data/chk.txt','r')
mail ='profits'


print (classifier.classify(extract_features(mail.split())))

f = open('my_classifier.pickle', 'wb') # pickle code just saves the classifier as a pickle file in project folder
pickle.dump(classifier, f)
f.close()
