s = raw_input("Enter the string in lowercase letters\n")
count = 0
for character in s:
   if character=='a' or character=='e' or character=='i' or character=='o' or character=='u':
       count+=1
print "Number of vowels: "+str(count)
   