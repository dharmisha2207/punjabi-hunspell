# -*- coding: utf-8 -*-
"""
Created on Tue Nov 8 08:15:03 2022
@author: Dharmisha Sharma
python program to take a thesaurus structured text data file 
and consolidate the duplicate thesaurus entries based on the word type
"""
import os, sys
import codecs

ne = 0          # number of entries in index
entry = ""      # current word being processed
wtype = ""      #type of the word
mset={}         #set for removing duplicates from the words list
data=[]         #for string entry, type and set
rec=""          #current string and related pieces
nm=0            #number of meaning for the current word
meaning=""      #current meaning and synonyms
p=0             #misc uses
encoding =""    #encoding used by text file

ifilename = "synonyms.out"

#Check if the file exists or not
if not os.path.isfile(ifilename):
    print("File [",ifilename,"] doesn't exist. Quitting")
    sys.exit()
else:
    #open the file with encoding
    with codecs.open(ifilename, encoding='utf-8') as fr:
        #create filename for index file
        ofilename = "th_pa_IN.dat" #os.path.splitext(ifilename)[0] + ".dat"
        #open the index file for storing data
        fw = open(ofilename, "w",encoding="utf-8")
        #read every line of the input file
        for rec in fr:
            ne = ne+1
            #if it's first line then extract the encoding 
            if ne == 1:        
                # top line of thesaurus provides encoding
                encoding = rec
                encoding = encoding.rstrip()
            else:                
                #read rest of the thesaurus line by line
                #first line of every block is an entry and meaning count
                #remove the trailing white spaces
                rec = rec.rstrip()
                #Split the line into parts separated by |
                spl = rec.split("|")
                #First extracted value is the entry and second is the number of it's types
                entry = spl[0]
                nm = int(spl[1])
                p = 0
                #read and calculate the length of each line
                while (p < nm):
                    #read the meanings of the word
                    meaning=fr.readline().rstrip()
                    #split the meanings
                    mns = meaning.split("|")
                    #First meaning is actually word form
                    wtype = mns[0]
                    #HAving extracted, delete word form from meaning
                    mns.pop(0)                                      
                    p = p + 1
                
                #create a set from the list to remove duplicates
                mset = set(mns)
                #store the entry, word form and list of synonyms in list
                lst = (entry, wtype, mset)
                #Append the list to data list
                data.append(lst)
                
                
        #Having collected all of the information
        #next data is sorted and then output the encoding, 
        #count and index data
        data.sort()
        
        #Combine the word with same forms while 
        #removing duplicates using sets
        ln = len(data)
        ndata=[]
        for i in range(ln-1):            
            if i < ln-1:
                if data[i][0] == data[i+1][0] and data[i][1] == data[i+1][1]:
                    ms = data[i][2].union(data[i+1][2])
                    lst = (data[i][0],data[i][1],ms)
                    ndata.append(lst)
                    data.pop(i+1)            
                else:
                    ndata.append(data[i])
                ln = len(data)
        
        fw.write(encoding)
        fw.write("\n")
        
        #Count the forms of word and accordingly 
        #write the data in the following form as required by LO
        #word|Form_Count
        #(form_1)|word1|word2|word3
        #(form_2)|word1|word2|word3
        ln = len(ndata)
        i = 0
        s = ""
        while i < ln-1:
            wcount = 1
            lst = list(ndata[i][2])
            s = ndata[i][1]
            for l in lst:
                s = s+"|"+l
            s = s + "\n"   
            j = i                
            while j < ln and ndata[j][0] == ndata[j+1][0]:
                lst = list(ndata[j+1][2])
                s = s + ndata[j+1][1]
                for l in lst:
                    s = s + "|" + l
                s = s + "\n"
                j = j + 1
                wcount += 1                
            i = j
            fw.write(ndata[i][0]+"|"+str(wcount)+"\n"+s)                
            i=i+1
       
fr.close() 
fw.close()
