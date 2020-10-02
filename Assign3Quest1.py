#Reading the contents of the file
print("Reading the contents of the file")
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    print(line)

#Regular expression for finding the message ID statement
print("\nExtraction of message-Id statement--------------------------------")
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x=re.findall(r'^Message-ID: <.*>',line)
    if len(x)>0:
    	for y in x:
    		s,c=y.split("Message-ID:")
    		print(c)
    
#Regular expression for finding the date
print("\nExtraction of date statement--------------------------------")
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x=re.findall(r'^Date: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -\d{4}',line)
    if len(x)>0:
    	print(x)


#Regular expression for finding the svn commit statements
print("\nExtraction of svn commit statement--------------------------------")
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x=re.findall(r'.*svn commit: (\w+)',line) #  for svn commit
    if len(x)>0:
    	print(x)




    


 
  
