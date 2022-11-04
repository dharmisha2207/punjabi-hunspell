
import os, sys
if os.path.isfile("synonymsbase.txt"):
    cl = cw = cc = 0
    with open("Synonyms.dic", "wb") as fw:        
        with open("Synonymsbase.txt", 'rb') as fr:
            for line in fr:
                str = line.decode()
                #print(str)
                words = str.split("\t")
                wtype = words[1].strip()
                str = words[0]
                words = str.split(",")
                #select all words root for once and alternate
                root = words[0]
                root1 = words[0] + "|1\n"
                fw.write(root1.encode())
                words.remove(root)
                #words.remove(wtype)
                wl = len(words)
                ws = "("+wtype+")|"
                for i in range(wl):
                    if i < wl-1:
                        ws += words[i]+"|"
                    else:
                        ws += words[i]
                ws +="\n"
                fw.write(ws.encode())
                cc += len(str)
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
