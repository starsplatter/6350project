# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:01:12 2015

@author: jrc88
"""
#document creation
# read in line from spreadsheet
    #get identifier, title, year
    #get text from address in spreadsheet
        #split text into thousand word chunks
    #output one line per chuck, stamped with identifier, title, year into csv
#throw out the first and last 1000 word chunk of each document

#author finder
# open an original text (pre-chunking)
    # regex to find 'by A'
    # print filename, A to new line in csv file

#year finder
    # for each file name
        #regex search for four digits in a row
        #print filename, year to to a row in a csv file

#collections of multiple capital letters -> authors, titles?




import csv
import codecs
import numpy as np
from scipy import dot
from scipy import linalg
import matplotlib
import os
import glob
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

def split_text(filename,n_words):
    input = open(filename, 'r')
    words = input.read()
    words = tokenizer.tokenize(words.lower())
    input.close()
    chunks= []
    current_chunk_words = []
    current_chunk_word_count = 0
    for word in words:
        current_chunk_words.append(word)
        current_chunk_word_count += 1
        if current_chunk_word_count == n_words:
            chunks.append(' '.join(current_chunk_words))
            current_chunk_words = []
            current_chunk_word_count = 0
    chunks.append(' '.join(current_chunk_words))
    return chunks
    
pulp_files = glob.glob("*/*story.txt")
chunk_length = 1000
chunks = []
writer = csv.writer(codecs.open('stories.txt', 'wb'))
for filename in pulp_files:
    chunk_counter = 0
    texts = split_text(filename,chunk_length)
    for text in texts:
        text = str.join(" ", text.splitlines())
        chunk = {'number': chunk_counter, 'filename':filename, 'text': text}
        chunks.append(chunk)
        chunk_counter += 1
        filename = filename.replace("/","_")
        filename = filename.replace(".","_")
        filename = filename.replace(" ","_")
        #if chunk_counter > 2:
        writer.writerow([filename+"_"+str(chunk_counter)+'\t'+filename+'\t'+text]) 

        #this looks right in python's editor and in sublime text, can't get excel to read it at all
  