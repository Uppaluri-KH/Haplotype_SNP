import numpy
import pandas as pd
import os
import sys

df = pd.read_excel("Haplo_SNPs_Unique.xlsx")
df['ALT'] = df['ALT'].str.split(',')
df = df.explode('ALT')
df = df.drop_duplicates(subset=['CHROM', 'POS', 'REF', 'ALT'])
vcf = pd.read_csv("/{}_final_DP.vcf".format(sys.argv[1], sys.argv[1]), comment= '#', sep = '\t', header=None, low_memory=False)
vcf.columns = ['CHROM', 'POS', 'rsID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'SAMPLE']
vcf['DP'] = vcf['SAMPLE'].str.split(':').str[3].fillna('0').astype(int)
vcf['HET'] = vcf['INFO'].str.extract(r'HET=(\d)')
vcf['HOM'] = vcf['INFO'].str.extract(r'HOM=(\d)')
# Create a new column 'Zygosity' based on conditions
vcf['Zygosity'] = ''
vcf.loc[vcf['HOM'] == '1', 'Zygosity'] = 'Homozygous'
vcf.loc[vcf['HET'] == '1', 'Zygosity'] = 'Heterozygous'
vcf.drop(columns=['HET', 'HOM'], inplace=True)
common = pd.merge(vcf, df, on = ['CHROM', 'POS', 'REF', 'ALT'], how = 'inner', sort = False)
common.to_excel("/{}_snp.xlsx".format(sys.argv[1], sys.argv[1]), index = False)
print(common)
