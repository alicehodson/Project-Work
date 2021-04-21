import pyfastx
from pathlib import Path

directory = Path('.')
output_files = list(directory.rglob('*'))
output_files = [fastq_string_file for fastq_string_file in output_files if '.fastq' in fastq_string_file.suffixes]
print(output_files)

idx = [3000, 512, 256, 128, 64]
for idx,(name,seq,qual,comment) in enumerate(pyfastx.Fastx('soil_sample_a.fastq')):
    count += 1
    reads_list.append(f">{name}\n{seq}")
    if count == num_reads:
      count = 0
      with open(f'{num_reads}_short_{read_file.name}', 'w') as fh:
        fh.write("\n".join(reads_list))
      reads_list = []
      break
