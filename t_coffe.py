from Bio import AlignIO
import subprocess

# Paths
tcoffee_exe = "/Users/omkar/miniconda3/bin/t_coffee"  # Path to T-Coffee executable
input_file = "/Users/omkar/Downloads/bb3_release/TEST/BB12001.tfa"  # Input TFA file
clustal_output_file = "/Users/omkar/Downloads/bb3_release/TEST/aligned_sequences.aln"  # T-Coffee Clustal output
msf_output_file = "/Users/omkar/Downloads/bb3_release/TEST/aligned_sequences.msf"  # Final MSF output

# Run T-Coffee to align sequences and generate Clustal output
tcoffee_cmd = [tcoffee_exe, "-infile", input_file, "-output", "clustalw_aln", "-outfile", clustal_output_file]
subprocess.run(tcoffee_cmd, check=True)

# Convert Clustal alignment to MSF using EMBOSS seqret
seqret_cmd = ["seqret", "-sequence", clustal_output_file, "-sformat1", "clustal", "-outseq", msf_output_file, "-osformat2", "msf"]
subprocess.run(seqret_cmd, check=True)

# Read and print the MSF alignment
alignment = AlignIO.read(msf_output_file, "msf")
print(alignment)