import pyfastx
from pathlib import Path

directory = Path('.')
output_files = list(directory.rglob('*'))
output_files = [fastq_string_file for fastq_string_file in output_files if '.fastq' in fastq_string_file.suffixes]
print(output_files)

def split_files (file_range) 
length = [3000, 512, 256, 128, 64]
for num_reads in length:
    reads_list = []
    count =  0
    for read_file in output_files:
        fx = pyfastx.Fastx(str(read_file))
       # for idx,(name,seq,qual,comment) in enumerate(pyfastx.Fastx('soil_sample_a.fastq', 0:3000, 3000:3512, 3512:3768, 3768:3896, 3896:3960)):
        for idx,(name,seq,qual,comment) in range(0, 3000)
        for idx,(name,seq,qual,comment) in range(3000, 3512)
        for idx,(name,seq,qual,comment) in range(3512, 3768)
        for idx,(name,seq,qual,comment) in range(3768, 3896)
        for idx,(name,seq,qual,comment) in range(3896, 3960)
            count += 1
            reads_list.append(f">{name}\n{seq}")
            if count == num_reads:
                count = 0
                with open(f'{num_reads}_short_{read_file.name}', 'w') as fh:
                    fh.write("\n".join(reads_list))
                reads_list = []
                break
~
