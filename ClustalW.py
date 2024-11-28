import os
import subprocess
from Bio.Align.Applications import ClustalwCommandline

# Define paths
clustalw_path = "/Users/manikumar/miniconda3/bin/clustalw2"
input_dir = "/Users/manikumar/Downloads/bb3_release/TEST/"
output_dir = input_dir  # Output MSF files will be saved in the same directory

# Get a list of all TFA files in the directory
tfa_files = [f for f in os.listdir(input_dir) if f.endswith(".tfa")]

# Process each TFA file
for tfa_file in tfa_files:
    tfa_path = os.path.join(input_dir, tfa_file)
    clustal_output_file = os.path.join(output_dir, f"{os.path.splitext(tfa_file)[0]}.aln")
    msf_output_file = os.path.join(output_dir, f"sequence_{os.path.splitext(tfa_file)[0]}.msf")  # MSF output file

    # Run ClustalW to generate alignment in Clustal format
    clustalw_cline = ClustalwCommandline(clustalw_path, infile=tfa_path)
    stdout, stderr = clustalw_cline()

    # Convert Clustal alignment to MSF using EMBOSS seqret
    seqret_command = [
        "seqret",
        "-sequence", clustal_output_file,
        "-sformat1", "clustal",
        "-outseq", msf_output_file,
        "-osformat2", "msf"
    ]
    subprocess.run(seqret_command, check=True)

    print(f"MSF alignment saved to: {msf_output_file}")
