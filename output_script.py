import time
import subprocess

def reads_output(file_name, size):
    with open(file_name, "r") as fh:
       subprocess.Popen(f'time kraken2 --db /home/mbyah11/kraken2-microbial-fatfree/ --use-names --threads 4 {file_name} --output zymo_{size}_run_{sample_letter}.output'.split()).communicate()

sample_letter = '0'
reads_output('zymo_log_4000_reads_0.fastq', 'OG')
reads_output('zymo_short_100_0.fasta', '100')
reads_output('zymo_short_200_0.fasta', '200')
reads_output('zymo_short_500_0.fasta', '500')
