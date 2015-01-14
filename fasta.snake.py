include: "constants.py"

include: "progs.snake.py"


rule __test_all_fasta__:
	input:
		ALL_FAS, ALL_FAIS

rule example_fasta:
	output:
		FA_EXAMPLE
	shell:
		"""
		curl --insecure -o {output[0]} ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Mycobacterium_tuberculosis_H37Rv_uid170532/NC_018143.fna
		"""

rule index_fa:
	output:
		"{filename}.fa.fai"
	input:
		PROG_SAMTOOLS,
		"{filename}.fa"
	shell:
		"{input[0]} faidx {input[1]}"		

rule index_fasta:
	output:
		"{filename}.fasta.fai"
	input:
		PROG_SAMTOOLS,
		"{filename}.fasta"
	shell:
		"{input[0]} faidx {input[1]}"		
