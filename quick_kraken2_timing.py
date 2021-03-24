import time
import subprocess

def reads_output(file_name, size):
    with open(file_name, "r") as fh:
       subprocess.Popen(f'time kraken2 --db /home/mbyah11/kraken2-microbial-fatfree/ --use-names --threads 4 --quick --memory-mapping {file_name} --output batch_{size}_run_{sample_letter}.output'.split()).communicate()

sample_letter = '0'
reads_output('3000_short_zymo_log_4000_reads_0.fastq', '3000')
reads_output('512_short_zymo_log_4000_reads_0.fastq', '512')
reads_output('256_short_zymo_log_4000_reads_0.fastq', '256')
reads_output('128_short_zymo_log_4000_reads_0.fastq', '128')
