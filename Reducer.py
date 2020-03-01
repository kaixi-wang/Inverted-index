#!/usr/bin/python

# read the results of mapper.py from STDIN and sum the occurrences of each word to a final count then output its results to STDOUT

# chmod +x  ./reducer.py

#from operator import itemgetter
import sys
from sys import stdin

#current_word = None
#current_count=0
#word=None
inverted_index={}

#input comes from STDIN
#create inverted index: inverted_index[word][docID]=count
for line in sys.stdin:
    word, stats = line.split('\t',1) # stats contains 'docID:count'
    docID, count= stats.split(':',1)
    count=int(count)
    if inverted_index.get(word) is not None:
        if inverted_index.get(word).get(docID) is not None:
            inverted_index[word][docID]+=count
        else:
            inverted_index[word][docID]=count
    else:
        inverted_index[word]={docID: count}
#postings_list=[]
for word in inverted_index.keys():
    postings_list = []
    [postings_list.append('%s:%d' % (doc,inverted_index[word][doc])) for doc in inverted_index[word]]
    postings_list=' '.join(postings_list)
    #print word,'\t', postings_list
    print '%s\t%s' % (word,postings_list)
    
