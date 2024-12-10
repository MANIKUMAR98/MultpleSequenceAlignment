import os
import subprocess
from Bio.Align.Applications import ClustalwCommandline
import time


clustalw_path = "/Users/manikumar/miniconda3/bin/clustalw2"
input_dir = "/Users/manikumar/Downloads/bb3_release/TEST/"
output_dir = input_dir


tfa_files = [f for f in os.listdir(input_dir) if f.endswith(".tfa")]
total_start_time = time.time()

for tfa_file in tfa_files:
    tfa_path = os.path.join(input_dir, tfa_file)
    clustal_output_file = os.path.join(output_dir, f"{os.path.splitext(tfa_file)[0]}.aln")
    msf_output_file = os.path.join(output_dir, f"sequence_{os.path.splitext(tfa_file)[0]}.msf")  # MSF output file

    clustalw_cline = ClustalwCommandline(clustalw_path, infile=tfa_path)
    stdout, stderr = clustalw_cline()

    seqret_command = [
        "seqret",
        "-sequence", clustal_output_file,
        "-sformat1", "clustal",
        "-outseq", msf_output_file,
        "-osformat2", "msf"
    ]
    subprocess.run(seqret_command, check=True)

    total_end_time = time.time()
    total_time_taken = total_end_time - total_start_time
    print(f"Total time taken for processing all files: {total_time_taken:.2f} seconds")

