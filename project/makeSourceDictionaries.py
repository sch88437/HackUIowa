
import wikipedia
import nltk
from nltk.corpus import wordnet as wn
from FileMaker import FileMaker
from DictionaryMaker import DictionaryMaker
import random
import os

os.chdir('.\\sourceFiles')

p = FileMaker('ENTP')
people=p.makeList()
print(people)

dictionaries=[]
for person in people:
    dictionaries.append(DictionaryMaker(person).getList())
    print(person)

#print(dictionaries)
m=[j for i in dictionaries for j in i]
#print(set(master))
master=[]
for i in range (250):
    j=random.randint(0,(len(m)-1))
    master.append(m[j])

print(master)

theDict=open('ENTPdictionary.txt','w')
for m in master:
    theDict.write(m)
    theDict.write(' ')
    
theDict.close()


'''
p = FileMaker('INTJ')
people=p.makeList()
dictionaries=[]
for person in people:
    #dictionaries.append(DictionaryMaker(person).getDictionary())
    d=DictionaryMaker(person)
    dictionaries.append(d.getDictionary)
print(dictionaries[0])

INTJ={}
for dictionary in dictionaries:
    #INTJ.update(dictionary)
    print(dictionary)
INTJ=(list(set(INTJ.keys())))

counterINTJ=0

vangogh=DictionaryMaker('Van Gogh').getDictionary()
for item in vangogh:
    if INTJ.index(item):
        counterINTJ+=1
    else:
        continue

print(counterINTJ)
'''
