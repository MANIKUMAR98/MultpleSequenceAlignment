from Bio import AlignIO
import subprocess


# Define paths
muscle_exe = "/Users/manikumar/miniconda3/bin/muscle"  # Path to the MUSCLE executable
input_file = "/Users/manikumar/Downloads/bb3_release/TEST/BB12001.tfa"  # Input file (TFA)
fasta_output_file = "/Users/manikumar/Downloads/bb3_release/TEST/aligned_sequences.fasta"  # Temporary output aligned file in FASTA
msf_output_file = "/Users/manikumar/Downloads/bb3_release/TEST/aligned_sequences.msf"  # Final output in MSF format

# Run MUSCLE to align the sequences and output in FASTA format
muscle_cmd = [muscle_exe, "-align", input_file, "-output", fasta_output_file]
subprocess.run(muscle_cmd, check=True)

# Convert the FASTA file to MSF using EMBOSS seqret
seqret_cmd = ["seqret", "-sequence", fasta_output_file, "-sformat1", "fasta", "-outseq", msf_output_file, "-osformat2", "msf"]
subprocess.run(seqret_cmd, check=True)

# Read and print the alignment result in MSF format
alignment = AlignIO.read(msf_output_file, "msf")
print(alignment)