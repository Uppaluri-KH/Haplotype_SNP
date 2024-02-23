# Haplotype_SNP

1. In this analysis considered the level 1A, 1B, 2A, 2B variants those are from the pharmgkb version4 updated database sheet.
2.Extracted the positional information for those variants from emsambl database. The supporting variants file contains the         Genes, rsID, CHROM, POS, REF, ALT columns.
3. This support file mapped with the 1232 Aigprx samples to retrieve the variants on the basis of CHROM, POS, REF, ALT columns.
4. Concatenated those files as a single file and created the new sample column with the file name of the samples.
5. From this final file extracted the respective samples counts for classes in Zygosity (HET, HOM).
6. Based on these counts calculated the K&H maf values. And also extracted the other population maf from the genomAd website. And compared those maf values for each rsID.
