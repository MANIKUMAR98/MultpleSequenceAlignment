# Comparative Analysis of Multiple Sequence Alignment (MSA) Algorithms

## Overview
This project evaluates the performance of five widely used Multiple Sequence Alignment (MSA) algorithms — **ClustalW**, **MAFFT**, **MUSCLE**, **ProbCons**, and **T-Coffee** — using the **BAliBASE3 benchmark dataset**. The goal is to analyze alignment accuracy, computational efficiency, and the ability to handle diverse datasets. This project also implements utilities to compute evaluation metrics such as **Sum-of-Pairs (SP) Score** and **Total Columns (TC) Score**.

1. **Frontend**: [Frontend](https://uflorida-my.sharepoint.com/:v:/g/personal/manikuma_honnena_ufl_edu/EToLoOhUUL5HpnVLnbYe0y4BJ3SYhAa3fVypYHyCvLzx2w?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=PoyqG6)

2. **Backend**: [Backend](https://uflorida-my.sharepoint.com/:v:/g/personal/chiplun_rushangs_ufl_edu/Ec38f4o3f8dKuX7WpW7JLq4BmIIDNlMYgD4JIU-YuaPpNw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=7z7lZP)


## Features
- Automates MSA for multiple input sequence files.
- Converts alignment outputs into MSF format for further analysis.
- Implements scoring and comparison using BAliBASE3 reference datasets.
- Provides a C-based scoring utility to evaluate alignment quality.

---

## Directory Structure
### Files
1. **`ClustalW.py`**  
   - Automates the alignment process using the ClustalW tool.  
   - Converts Clustal alignment outputs to MSF format using `seqret`.  
   - Input: `.tfa` files; Output: `.msf` files.  

2. **`mafft.py`**  
   - Uses the MAFFT tool to align sequences.  
   - Converts alignment outputs to MSF format using `seqret`.  
   - Input: `.tfa` files; Output: `.msf` files.

3. **`muscle.py`**  
   - Automates sequence alignment using MUSCLE.  
   - Converts alignment outputs to MSF format using `seqret`.  
   - Input: `.tfa` files; Output: `.msf` files.

4. **`probcons.py`**  
   - Executes sequence alignment using ProbCons.  
   - Converts FASTA alignment outputs to MSF format using `seqret`.  
   - Input: `.tfa` files; Output: `.msf` files.

5. **`t_coffee.py`**  
   - Runs T-Coffee for sequence alignment.  
   - Converts Clustal alignment outputs to MSF format using `seqret`.  
   - Input: `.tfa` files; Output: `.msf` files.

6. **`bali_score.c`**  
   - A C program to calculate SP and TC scores for alignments.  
   - Compares test alignment with reference alignment from BAliBASE3.  
   - Input: Reference and test `.msf` files; Output: SP and TC scores.

---

## Requirements
### Tools
- **MSA Tools**  
  - ClustalW  
  - MAFFT  
  - MUSCLE  
  - ProbCons  
  - T-Coffee  

- **Utility Tools**  
  - EMBOSS `seqret` for format conversion (e.g., FASTA/Clustal to MSF).

- **Languages**  
  - Python (for automation scripts)  
  - C (for scoring utility)  

### Python Libraries
- `BioPython` for parsing and analyzing alignments.  
- `subprocess` for running external commands.

### Datasets
- BAliBASE3 benchmark dataset.  

---

## Setup and Usage

### 1. Install Dependencies
- **Install MSA Tools**  
  Ensure ClustalW, MAFFT, MUSCLE, ProbCons, and T-Coffee are installed and added to your `PATH`.  

- **Install EMBOSS Suite**  
  Install EMBOSS and verify `seqret` is available.

- **Install Python Libraries**  
  ```bash
  pip install biopython
  ```
### 2. Run Alignments  
Use the corresponding Python script for each algorithm. For example:  

### Run MAFFT:
To run MAFFT for aligning your sequences, execute the following command:
  ```bash
  python mafft.py
  ```


### Each Script

1. **Processes `.tfa` Input Files**: Reads input sequence files in `.tfa` format.
2. **Aligns Sequences**: Performs multiple sequence alignment using the respective tool.
3. **Converts Results to MSF Format**: Transforms alignment outputs into the MSF format for downstream analysis.

---

### 3. Evaluate Alignments

To calculate SP and TC scores for your alignments, compile and run the `bali_score.c` program:

```bash
gcc -o bali_score bali_score.c
./bali_score reference_alignment.msf test_alignment.msf
```

### 4. Output Files
- **Intermediate Files**: Alignment outputs in FASTA or Clustal format.
- **Final Files**: MSF files for downstream evaluation.

---

## Project flow

1. **Input**: Provide `.tfa` files in the working directory.
2. **Execution**: Scripts automate MSA and format conversion.
3. **Evaluation**: Use the C program to assess the quality of alignments.

---

## Results and Observations
- **SP and TC Scores**: Evaluate alignment quality using BAliBASE3 reference alignments.
- **Computational Time**: Assess the speed of different tools.
- **Accuracy Trade-offs**: ProbCons is highly accurate but slower; MUSCLE is faster but slightly less accurate.

---

## Authors
- **Manikumar Honnenahalli Lakshminarayana Swamy** (manikuma.honnena@ufl.edu)
- **Omkar Bhabad** (omkar.bhabad@ufl.edu)
