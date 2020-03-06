import pysrt
import obo 

subs = pysrt.open("Corpse.Bride.2005.1080p.BrRip.x264.BOKUTOX.YIFY.srt")
#subs = pysrt.open("Corpse.Bride.2005.720p.BDRip.x264-PROGRESS.txt")
#print(len(subs))
wordstring = ""
for i in subs:
    wordstring += i.text + " "

#text = obo.stripTags(wordstring).lower()
text = wordstring.lower()
#print(text)
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)
counter = 0
#for freq in range(5,1,-1):
#    f = open("Corpse_word_freq-%d.txt"%freq)
out = open("Corpse_word_freq.txt", "w")
freq = -1
for c, w in sorteddict:
    if freq != c:
        if freq != -1:
            msg= "-"*10 + " Summery: freq=%d count=%d "%(freq, counter) + "-"*10 + "\n"
            print(msg)
            out.write(msg)
            counter = 0
        
 
        freq = c
        
        msg="-"*10 + "Word with freq = %d"%c + "-"*10 + "\n"
        print(msg)
        out.write(msg)
            
    counter += 1
    #if c >= 2:
    #print(c, str(w))
        #counter = counter + 1
        #print(counter, str(w))
    #if counter >= 1000 :
    #    break
    msg = str(w) + "\n"
    print(msg)
    out.write(msg)


msg= "-"*10 + " Summery: freq=%d count=%d "%(freq, counter) + "-"*10 + "\n"
print(msg)
out.write(msg)
out.close()

