
from FileMaker import FileMaker
import wikipedia
from DictionaryMaker import DictionaryMaker
import os

#print(os.getcwd())

p = "Donald Trump"
person=DictionaryMaker(p)
os.chdir('.\\sourceFiles')


#ANALYSTS
INTJ=0
INTJvalues=open('INTJdictionary.txt').read().split()

INTP=0
INTPvalues=open('INTPdictionary.txt').read().split()

ENTJ=0
ENTJvalues=open('ENTJdictionary.txt').read().split()

ENTP=0
ENTPvalues=open('ENTPdictionary.txt').read().split()


#DIPLOMATS
INFJ=0
INFJvalues=open('INFJdictionary.txt').read().split()

INFP=0
INFPvalues=open('INFPdictionary.txt').read().split()

ENFJ=0
ENFJvalues=open('ENFJdictionary.txt').read().split()

ENFP=0
ENFPvalues=open('ENFPdictionary.txt').read().split()

#SENTINELS
ISTJ=0
ISTJvalues=open('ISTJdictionary.txt').read().split()

ISFJ=0
ISFJvalues=open('ISFJdictionary.txt').read().split()

ESTJ=0
ESTJvalues=open('ESTJdictionary.txt').read().split()

ESFJ=0
ESFJvalues=open('ESFJdictionary.txt').read().split()

#EXPLORERS
ISTP=0
ISTPvalues=open('ISTPdictionary.txt').read().split()

ISFP=0
ISFPvalues=open('ISFPdictionary.txt').read().split()

ESTP=0
ESTPvalues=open('ESTPdictionary.txt').read().split()


ESFP=0
ESFPvalues=open('ESFPdictionary.txt').read().split()


#print(person.getList())

for item in person.getList():
    if item in ENFJvalues:
        ENFJ+=1
        
    if item in ENFPvalues:
        ENFP+=1
        
    if item in ENTJvalues:
        ENTJ+=1

    if item in ENTPvalues:
        ENTP+=1

    if item in ESFJvalues:
        ESFJ+=1

    if item in ESFPvalues:
        ESFP+=1

    if item in ESTJvalues:
        ESTJ+=1

    if item in ESTPvalues:
        ESTP+=1

    if item in INFJvalues:
        INFJ+=1

    if item in INFPvalues:
        INFP+=1

    if item in INTJvalues:
        INTJ+=1

    if item in INTPvalues:
        INTP+=1

    if item in ISFJvalues:
        ISFJ+=1

    if item in ISFPvalues:
        ISFP+=1

    if item in ISTJvalues:
        ISTJ+=1

    if item in ISTPvalues:
        ISTP+=1

nameListy=['ENFJ','ENFP','ENTJ','ENTP','ESFJ','ESFP','ESTJ','ESTP','INFJ','INFP','INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP']
listy=[ENFJ,ENFP,ENTJ,ENTP,ESFJ,ESFP,ESTJ,ESTP,INFJ,INFP,INTJ,INTP,ISFJ,ISFP,ISTJ,ISTP]
m=max(listy)
index=listy.index(m)
print(p+" "+nameListy[index])
