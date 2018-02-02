#fileopen=open('sun.txt')
#read1=fileopen.readlines()
count=0
##print(type(read1))
##print ("Read lines: %s",  (read1))
#fileopen.close()
#
#while read1:
#    count=count+1
#print(count)


with open('sun.txt') as f:
   for line in f:
        count=count+1
print('The total number of lines in sun.txt is',count)
