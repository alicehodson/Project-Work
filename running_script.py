import time
import subprocess

def reads_output(file_name, tsv_file_name, raw_file_name):
    with open(file_name, "r") as fh:
       subprocess.Popen(f'time centrifuge -x /home/django/Centrifuge_index/abv -f -p 4 {file_name} --report-file {raw_file_name} -S{tsv_file_name}'.split()).communicate()

reads_output('2000_b.fasta', 'centrifuge_2000_run_b.raw', 'centrifuge_2000_run_b.tsv')
reads_output('1000_b.fasta', 'centrifuge_1000_run_b.raw', 'centrifuge_1000_run_b.tsv')
reads_output('500_b.fasta', 'centrifuge_500_run_b.tsv', 'centrifuge_500_run_b.raw')
reads_output('200_b.fasta', 'centrifuge_200_run_b.tsv', 'centrifuge_200_run_b.raw')
reads_output('100_b.fasta', 'centrifuge_100_run_b.tsv', 'centrifuge_100_run_b.raw')
