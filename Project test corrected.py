fastq = open("FAL00432.fastq","rt")
lines = fastq.readlines()

n=100
file = open("100.txt","w")
i=0
for line in lines:
    i=i+1
    if (i+2) % 4 == 0:
        file.write(line[0:n]+"\n")
        


fastq.close()
file.close()  
