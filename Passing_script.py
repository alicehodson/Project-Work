import pandas as pd
import numpy as np
from pathlib import Path

def check_group(group):
    """
       Check a group from dataframe to see if a read at different lengths has the same classification as the original length
    """
    # Get the true classification from the longest reads
    true_species = group[group['file'].eq(f'OG_reads_{sample_letter}')]['classification'].iloc[0]
    print(true_species)
    # return a 1 if it's true across the group and 0 if not
    group['positives']= np.where(group['classification']==true_species, 1,0)
    # add our calcualtions to the results dictionary
    for row in group[['positives', 'file']].to_dict(orient="records"):
        positive = row["positives"]
        if positive:
            results[row["file"]][0] += 1
        else:
            results[row["file"]][1] += 1
results = {}

# sample letter to look for in the files
sample_letter= 'a'
# direcotry to look in . is shorthand for the current directory
directory = Path('.')
# list of all files that match our search pattern
output_files = list(directory.rglob(f'*{sample_letter}.output'))
df = pd.DataFrame()
#for each file
for file_path in output_files:
    temp_df =pd.read_csv(file_path, sep='\t', names = ['classified', 'read_ID', 'classification', 'length', 'LCA_Mapping'])
    temp_df['file'] = file_path.stem
    df = df.append(temp_df)
    results[file_path.stem] = [0,0,0]
# only classified reads
df = df[df['classified'].eq('C')]
print(df['file'].unique())
# group by the read_id across all the files and that they were classified
gb = df.groupby(['read_ID', 'classified',])
# for each group call the functon - note could be switched to .apply now which would be faster!
for name,group in gb:
    check_group(group)

print(results)
