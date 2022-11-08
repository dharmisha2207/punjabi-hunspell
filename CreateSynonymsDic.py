# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:53:44 2022
@author: Dharmisha Sharma
Program to convert Wordnet to Thesaurus format
Where an entry in would be of the following form
word1|WordTypes
(WordType)|word2|word3|word4
"""
import os, sys
#Check if the source/input file exists
if os.path.isfile("synonymsbase.txt"):
    cl = cw = cc = 0
    #open the outfile for storing converted Thesaurus
    with open("Synonyms.out", "wb") as fw:  
        #Specify the encouding system used in the output file
        fw.write("UTF-8\n".encode())
        #Open the input file
        with open("Synonymsbase.txt", 'rb') as fr:
            #read each line form the input file
            for line in fr:
                #Decode the read data
                str = line.decode()
                #Initially, split the string into two parts words and wordtype
                words = str.split("\t")
                #remove any leading or trailing spaces and store the word type
                wtype = words[1].strip()
                #store the words in string
                str = words[0]
                #Further the split the words into individual words
                words = str.split(",")
                #select all words root for once and alternate
                wl = len(words)
                #for each word in to words treat the first word as the
                #root words and remaining words as the synonyms
                #Then place the root word at the end and use the next
                #word as the root word. This way, make all the conbination
                #for synonyms
                for i in range(wl):                    
                    root = words[0]
                    root1 = words[0].strip() + "|1\n"
                    #Remove the root word from words
                    words.remove(root)
                    wl1 = len(words)
                    ws = "("+wtype+")|"
                    for j in range(wl1):
                        if j < wl1-1:
                            ws += words[j].strip()+"|"
                        else:
                            ws += words[j].strip()
                    ws +="\n"
                    #write the root word and it's synonyms in file
                    fw.write(root1.encode())
                    fw.write(ws.encode())
                    #Store the root word at the end of words
                    words.append(root)
            else:
                # No more lines to be read from file
                print("Done")
            fr.close()         
            fw.close()
else:
    print("File not found")
    sys.exit()
