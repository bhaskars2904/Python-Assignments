s = raw_input("Enter the string in lowercase letters\n")
index=0
max_index=0
length=1
max_length=1
for i in range(len(s)-1):
    if s[i+1]>=s[i]:
        length += 1
        print s[index]+" "+s[max_index]+" "+str(max_length)+" "+str(length)
    else:
        if max_length<length:
            max_length = length
            max_index = index
        index = i+1
        length = 1
        print s[index]+" "+s[max_index]+" "+str(max_length)+" "+str(length)
if(length<=max_length):
    print s[max_index:max_index+max_length]
else:
    print s[index:index+length]
