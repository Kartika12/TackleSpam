import pickle
import nltk
import os, fnmatch

def classif1(str):
    f = open('my_classifier1.pickle', 'rb')
    classifier = pickle.load(f)
    mail =str

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
                    advertisment_mails.append((word,'Advertisment'))

    forgery_mails=[]
    for textFile in findFiles(r'Data/forgery','*.txt'):
       fileobj1=open(textFile,'r')
       for line in fileobj1:
          for word in line.split():
             if len(word)>3:
                forgery_mails.append((word,'Forgery/Lottery'))

    mails1=[]
    for (words,sentiment) in advertisment_mails + forgery_mails :
        words_filtered = [e.lower() for e in words.split() if len(e)>=3]
        mails1.append((words_filtered,sentiment))


    def get_words_in_mails(mails1):
       all_words = []
       for (words,sentiment) in mails1:
          all_words.extend(words)
       return all_words

    def get_word_features(wordlist):
       wordlist = nltk.FreqDist(wordlist)
       word_features = wordlist.keys()
       return word_features

    word_features = get_word_features(get_words_in_mails(mails1))

    def extract_features(document):
       features=document
       document_words = set(document)
       features = {}
       for word in word_features:
          features['contains(%s)'%word] = (word in document_words)
       return features

    result=(classifier.classify(extract_features(mail.split())))

    return result
    f.close()