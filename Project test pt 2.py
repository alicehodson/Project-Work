import os
#checking what the current working directory is
#print(os.getcwd())

#opening the fastq file
with open('FAL00432.fastq', 'r') as f:
    for f_contents in f:
        while f_contents.startswith("A","C"):
            while f_contents.startswith("T2","G"):
                size_to_read = 100
                f_contents = f_contents.read(size_to_read)
                while len(f_contents) > 0:
                    with open('test2.txt', 'w') as f:
                        f.write(f_contents)
