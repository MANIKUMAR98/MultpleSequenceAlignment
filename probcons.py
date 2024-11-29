from Bio import AlignIO
import subprocess

# Paths
probcons_exe = "/Users/manikumar/miniconda3/bin/probcons"  # Path to ProbCons executable
input_file = "/Users/manikumar/Downloads/bb3_release/TEST/BB12001.tfa"  # Input TFA file
fasta_output_file = "/Users/manikumar/Downloads/bb3_release/TEST/aligned_sequences.fasta"  # Temporary FASTA output
msf_output_file = "/Users/manikumar/Downloads/bb3_release/TEST/aligned_sequences.msf"  # Final MSF output

# Run ProbCons to align sequences and output in FASTA format
probcons_cmd = [probcons_exe, input_file]
with open(fasta_output_file, "w") as fasta_out:
    subprocess.run(probcons_cmd, stdout=fasta_out, check=True)

# Convert the FASTA file to MSF format using EMBOSS seqret
seqret_cmd = ["seqret", "-sequence", fasta_output_file, "-sformat1", "fasta", "-outseq", msf_output_file, "-osformat2", "msf"]
subprocess.run(seqret_cmd, check=True)

# Read and print the MSF alignment
alignment = AlignIO.read(msf_output_file, "msf")
print(alignment)
