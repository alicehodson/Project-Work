import time
import subprocess

def reads_output(fasta_file, paf_file_name):
    fh = open(f'{paf_file_name}_{sample_letter}.paf', 'w')
    subprocess.call((f'time minimap2 -x map-ont --secondary=no /home/stxaspa/references/zymo/D6322.refseq/Genomes/zymo_D6322_refseq_all.mmi {fasta_file}'.split()), stdout = fh)

sample_letter = '0'
reads_output('2000_short_3000_0.fasta', '2000_unique_3000')
reads_output('1000_short_3000__0.fasta', '1000_unique_3000')
reads_output('500_short_3000_0.fasta', '500_unique_3000')
reads_output('200_short_3000_0.fasta', '200_unique_3000')
reads_output('100_short_3000_0.fasta', '100_unique_3000')
reads_output('2000_short_512_0.fasta', '2000_unique_512')
reads_output('1000_short_512__0.fasta', '1000_unique_512')
reads_output('500_short_512_0.fasta', '500_unique_512')
reads_output('200_short_512_0.fasta', '200_unique_512')
reads_output('100_short_512_0.fasta', '100_unique_512')
reads_output('2000_short_256_0.fasta', '2000_unique_256')
reads_output('1000_short_256__0.fasta', '1000_unique_256')
reads_output('500_short_256_0.fasta', '500_unique_256')
reads_output('200_short_256_0.fasta', '200_unique_256')
reads_output('100_short_256_0.fasta', '100_unique_256')
reads_output('2000_short_128_0.fasta', '2000_unique_128')
reads_output('1000_short_128__0.fasta', '1000_unique_128')
reads_output('500_short_128_0.fasta', '500_unique_128')
reads_output('200_short_128_0.fasta', '200_unique_128')
reads_output('100_short_128_0.fasta', '100_unique_128')
reads_output('2000_short_64_0.fasta', '2000_unique_64')
reads_output('1000_short_64_0.fasta', '1000_unique_64')
reads_output('500_short_64_0.fasta', '500_unique_64')
reads_output('200_short_64_0.fasta', '200_unique_64')
reads_output('100_short_64_0.fasta', '100_unique_64')
reads_output('2000_0.fasta', '2000_unique')
reads_output('1000_0.fasta', '1000_unique')
reads_output('500_0.fasta', '500_unique')
reads_output('200_0.fasta', '200_unique')
reads_output('100_0.fasta', '100_unique')
reads_output('3000_short_unique_0.fasta', '3000_unique_OG')
reads_output('512_short_unique_0.fasta', '512_unique_OG')
reads_output('256_short_unique_0.fasta', '256_unique_OG')
reads_output('128_short_unique_0.fasta', '128_unique_OG')
reads_output('64_short_unique_0.fasta', '64_unique_OG')
reads_output('zymo_log_4000_reads_0.fasta', 'OG_unique')
