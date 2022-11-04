# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:53:44 2022

@author: DVS
"""
import os, sys
if os.path.isfile("synonymsbase.txt"):
    cl = cw = cc = 0
    with open("Synonyms.dat", "wb") as fw:  
        fw.write("UTF-8\n".encode())
        with open("Synonymsbase.txt", 'rb') as fr:
            for line in fr:
                str = line.decode()
                #print(str)
                words = str.split("\t")
                wtype = words[1].strip()
                str = words[0]
                words = str.split(",")
                #select all words root for once and alternate
                wl = len(words)
                for i in range(wl):                    
                    root = words[0]
                    root1 = words[0].strip() + "|1\n"
                    #fw.write(root1.encode())
                    words.remove(root)
                    #words.remove(wtype)
                    wl1 = len(words)
                    ws = "("+wtype+")|"
                    for j in range(wl1):
                        if j < wl1-1:
                            ws += words[j].strip()+"|"
                        else:
                            ws += words[j].strip()
                    ws +="\n"
                    fw.write(root1.encode())
                    fw.write(ws.encode())
                    words.append(root)
            else:
                # No more lines to be read from file
                print("EOF reached")
            fr.close()         
            fw.close()
            
            #print("Lines -> ", cl)
            #print('Words -> ', cw)
            #print('Chars -> ', cc)
else:
    print("File not found")
    sys.exit()
