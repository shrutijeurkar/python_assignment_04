fo=open('sun.txt','r')
read1=fo.readlines()
read2=int(input("Give number of lines you want to read: "))
#mean = 0
for lines in range(read2):
    print(read1[lines])

