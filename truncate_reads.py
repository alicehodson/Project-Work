import time
import pyfastx

def shorten_reads(file_name, num_bases):
    with open(file_name, "w") as fh:

        for name, seq, qual in pyfastx.Fastq('FAL00432.fastq', build_index=False):
            fh.write(f">{name}\n{seq[:num_bases]}\n")

if __name__ == '__main__':
    shorten_reads('short_fastq_100.fastq', 100)
    shorten_reads('short_fastq_200.fastq', 200)
    shorten_reads('short_fastq_500.fastq', 500)
