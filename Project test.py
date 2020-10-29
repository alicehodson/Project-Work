import os
#checking what the current working directory is
print(os.getcwd())

#opening the fastq file
with open('FAL00432.fastq', 'r') as In:
    for f in In:
        if In.startswith("A", "G", "T", "C"):
            f.write(range[0:101])
            f.write(range[0:201])
            f.write(range[0:501])
