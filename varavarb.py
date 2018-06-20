import re
while True:
    vara = raw_input("Enter vara\n")
    if len(vara)==0:
        print("Invalid input")
        continue
    break
while True:
    varb = raw_input("Enter varb\n")
    if len(varb)==0:
        print("Invalid input")
        continue
    break

p = re.compile('^(-{0,1})([0-9]+)\.{0,1}([0-9]{0,}$)')

if p.match(vara):
    flaga=True
else:
    flaga=False
    
if p.match(varb):
    flagb=True
else:
    flagb=False
    
if flaga==False or flagb==False:
    print "String involved"
elif float(vara)>float(varb):
    print "bigger"
elif float(vara)<float(varb):
    print "smaller"
else:
    print "equal"
    