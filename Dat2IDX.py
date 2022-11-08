# -*- coding: utf-8 -*-
"""
Created on Sat Nov 2 21:20:03 2022
@author: Dharmisha Sharma
python program to take a thesaurus structured text data file 
and create the proper sorted index file (.idx)
"""
import os, sys
import codecs

# main routine
ne = 0          # number of entries in index
tindex=[]       # list containing word and it's offset in the file
foffset = 0     # file position offset into thesaurus
rec=""          # current string and related pieces
rl=0            # misc string length     
entry=""        # current word being processed
nm=0            # number of meaning for the current word
meaning=""      # current meaning and synonyms
p=""            # misc uses
encoding =""    # encoding used by text file

ifilename = "th_pa_IN.dat"#input("Enter the name of the file containing thesaurus -> ")

#Check if the file exists or not
if not os.path.isfile(ifilename):
    print("File [",ifilename,"] doesn't exist. Quitting")
    sys.exit()
else:
    #open the file with encoding
    with codecs.open(ifilename, encoding='utf-8') as fr:
        #create filename for index file
        ofilename = os.path.splitext(ifilename)[0] + ".idx"
        #open the index file for storing data
        fw = open(ofilename, "w",encoding="utf-8")
        #read every line of the input file
        for rec in fr:
            ne = ne+1
            #if it's first line then extract the encoding 
            if ne == 1:        
                # top line of thesaurus provides encoding
                encoding = rec
                foffset = foffset + len(encoding)
                encoding = encoding.rstrip()
            else:                
                # read thesaurus line by line
                # first line of every block is an entry and meaning count
                #encode the find the length of the string
                rl = len(rec.encode("UTF-8"))
                #remove the trailing white spaces
                rec = rec.rstrip()
                #Split the line into parts separated by |
                spl = rec.split("|")
                #First extracted values is the entry and second is the number of it's types
                entry = spl[0]
                nm = int(spl[1])
                p = 0
                #read and calculate the length of each line
                while (p < nm):
                    meaning=fr.readline()
                    rl = rl + len(meaning.encode("UTF-8"))
                    meaning = meaning.rstrip()
                    p = p + 1
                    
                #store the word and it's offset in a list
                tindex.append(entry +"|"+str(foffset))
                foffset = foffset + rl
                
        #Having collected all of the information
        #next data is sorted and then output the encoding, 
        #count and index data
        tindex.sort()       
        fw.write(encoding)
        fw.write("\n")
        ne = ne-1
        fw.write(str(ne))
        fw.write("\n")        
        for d in tindex:
            fw.write(d)
            fw.write("\n")
        
fr.close() 
fw.close()


   
