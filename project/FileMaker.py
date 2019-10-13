import wikipedia
import nltk
from nltk.corpus import wordnet as wn

class FileMaker:

    def __init__(self,name):
        self.name=name
        self.file=name+'.txt'

    def makeList(self):
        file = open(self.file,'r')
        listy=[]
        for line in file:
            #print(line)
            listy.append(line)
        return listy

    '''
pd=PersonalityDictionary('INTJ')
(pd.makeList())
'''
