def split_file(lines_per_file, small_file_name):
  with open('really_big_file.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()
        
sample_letter = 'a'        
split_file(3000, 'unique_3000_batch_reads_f{sample_letter}.fasta')
split_file(512, 'unique_512_batch_reads_f{sample_letter}.fasta')
split_file(256, 'unique_256_batch_reads_f{sample_letter}.fasta')
split_file(128, 'unique_128_batch_reads_f{sample_letter}.fasta')
split_file(64, 'unique_64_batch_reads_f{sample_letter}.fasta')
