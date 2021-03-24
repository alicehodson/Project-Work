import time
import subprocess

def reads_output(file_name, tsv_file_name, raw_file_name):
    with open(file_name, "r") as fh:
       subprocess.Popen(f'time centrifuge -x /home/django/Centrifuge_index/abv -q -p 4 -k 1 {file_name} --report-file {raw_file_name} -S{tsv_file_name}'.split()).communicate()

reads_output('3000_short_zymo_log_4000_reads_0.fastq', 'centrifuge_3000_run_0.raw', 'centrifuge_3000_run_0.tsv')
reads_output('512_short_zymo_log_4000_reads_0.fastq', 'centrifuge_512_run_0.raw', 'centrifuge_512_run_0.tsv')
reads_output('256_short_zymo_log_4000_reads_0.fastq', 'centrifuge_256_run_0.tsv', 'centrifuge_256_run_0.raw')
reads_output('128_short_zymo_log_4000_reads_0.fastq', 'centrifuge_128_run_0.tsv', 'centrifuge_128_run_0.raw')
reads_output('64_short_zymo_log_4000_reads_0.fastq', 'centrifuge_64_run_0.tsv', 'centrifuge_64_run_0.raw')
