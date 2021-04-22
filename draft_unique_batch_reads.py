import pyfastx
from pathlib import Path

directory = Path('.')
output_files = list(directory.rglob('*'))
output_files = [fastq_string_file for fastq_string_file in output_files if '.fastq' in fastq_string_file.suffixes]
print(output_files)


def unique_read(num_reads, file_number):
    reads_list = []
    count = 0
    sample_letter = 'a'
    idx = [0,3000], [3000,3512], [3512,3768], [3768,3896], [3896,3960]
    for idx,(name,seq,qual,comment) in enumerate(pyfastx.Fastx('soil_sample_a.fastq')):
        count += 1
        reads_list.append(f">{name}\n{seq}")
        if count == num_reads:
            with open(f'{file_number}_short_unique_{sample_letter}.fastq', 'w') as fh:
                fh.write("\n".join(reads_list))
            reads_list = []
            break

unique_read(3000, '3000')
unique_read(3512, '512')
unique_read(3768, '256')
unique_read(3896, '128')
unique_read(3960, '64')
