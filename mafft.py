import os
import subprocess
import glob

def process_files():
    # Get all input files matching the pattern BBnnnnn.tfa
    input_files = glob.glob("BB*.tfa")
    
    for input_file in input_files:
        # Define the intermediate and final output filenames
        base_name = os.path.splitext(input_file)[0]  # Remove .tfa extension
        aligned_file = f"aligned_{base_name}.fasta"  # Intermediate MAFFT output
        msf_file = f"out_{base_name}.msf"  # Final MSF output
        
        try:
            # Run MAFFT alignment
            print(f"Running MAFFT on {input_file}...")
            subprocess.run(
                ["mafft", "--auto", input_file],
                stdout=open(aligned_file, "w"),
                stderr=subprocess.PIPE,
                check=True
            )
            print(f"Alignment completed: {aligned_file}")
            
            # Convert FASTA to MSF format using seqret
            print(f"Converting {aligned_file} to MSF format...")
            subprocess.run(
                ["seqret", "-sequence", aligned_file, "-outseq", msf_file, "-osformat2", "msf"],
                stderr=subprocess.PIPE,
                check=True
            )
            print(f"MSF file generated: {msf_file}")
        
        except subprocess.CalledProcessError as e:
            print(f"Error processing {input_file}: {e}")
            continue

if __name__ == "__main__":
    process_files()
