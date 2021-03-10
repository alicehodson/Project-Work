import pandas as pd

df = pd.read_csv('zymo_OG_run_0.output', sep='\t', names = ['classified', 'read_ID', 'classification', 'length', 'LCA_Mapping'])
print(df.groupby('classified')['length'].describe)
