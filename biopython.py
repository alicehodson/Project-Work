from Bio import SeqIO

File_100=open("file100.txt", "w")

for record in SeqIO.parse("FAL00432.fastq", "fastq"):
    File_100.write(str(record.seq[:100])+"\n")

File_100.close()



File_200=open("file200.txt", "w")

for record in SeqIO.parse("FAL00432.fastq", "fastq"):
    File_200.write(str(record.seq[:200])+"\n")


File_200.close()



File_500=open("file500.txt", "w")

for record in SeqIO.parse("FAL00432.fastq", "fastq"):
    File_500.write(str(record.seq[:500])+"\n")

File_500.close()
