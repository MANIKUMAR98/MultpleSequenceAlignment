import os
import time
import subprocess
from Bio import AlignIO

# Paths
probcons_exe = "/Users/manikumar/miniconda3/bin/probcons"
input_dir = "/Users/manikumar/Downloads/bb3_release/TEST/"
output_dir = input_dir

tfa_files = [f for f in os.listdir(input_dir) if f.endswith(".tfa")]

total_start_time = time.time()

for tfa_file in tfa_files:
    file_start_time = time.time()

    input_file = os.path.join(input_dir, tfa_file)
    fasta_output_file = os.path.join(output_dir, f"{os.path.splitext(tfa_file)[0]}_aligned.fasta")
    msf_output_file = os.path.join(output_dir, f"{os.path.splitext(tfa_file)[0]}_aligned.msf")

    try:

        probcons_cmd = [probcons_exe, input_file]
        with open(fasta_output_file, "w") as fasta_out:
            subprocess.run(probcons_cmd, stdout=fasta_out, check=True)

        seqret_cmd = ["seqret", "-sequence", fasta_output_file, "-sformat1", "fasta", "-outseq", msf_output_file, "-osformat2", "msf"]
        subprocess.run(seqret_cmd, check=True)

        alignment = AlignIO.read(msf_output_file, "msf")
        print(f"Alignment for {tfa_file}:\n{alignment}")

        file_end_time = time.time()
        print(f"Time taken for {tfa_file}: {file_end_time - file_start_time:.2f} seconds")

    except Exception as e:
        print(f"Error processing {tfa_file}: {e}")

total_end_time = time.time()
print(f"Total time taken for processing all files: {total_end_time - total_start_time:.2f} seconds")
