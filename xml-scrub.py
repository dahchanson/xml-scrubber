import sys
import re

if len(sys.argv) != 2:
    print "incorrect argument count %d, 2 expected" %(len(sys.argv))

dataf = sys.argv[1]

with open(dataf, "r") as f:
    databuf = f.read()

filtertag = re.compile('<TRNTYPE>.*?</TRNTYPE>')
scrubdata= re.sub(filtertag, '', databuf)

scrubf = dataf.replace(".qfx", "-scrub.qfx")
f = open(scrubf, "w")
f.write(scrubdata)
f.close()
