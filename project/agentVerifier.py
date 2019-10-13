
import wikipedia

filename='ESFP.txt'
with open(filename,'r') as f:
    for line in f:
        if(wikipedia.search(line))==None:
            print(line+" NOT FOUND")
            break

print (filename+" GOOD TO GO")
