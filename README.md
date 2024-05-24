# Prom to TextGrid Converter

This repository contains scripts to convert `.prom` files into TextGrid format. The `.prom` files are the output of the Wavelet Prosody Toolkit. The main script, `prom_to_textgrid.py`, reads `.prom` files and generates corresponding TextGrid files with prominence and boundary strength tiers.

## Requirements

To install the required Python packages, use the provided `install_requirements.py` script.

### Installing Requirements

1. Ensure you have `pip` installed.
2. Run the following command to install the required packages:
   ```sh
   python install_requirements.py
Usage
Step 1: Generate .prom Files
First, you need to generate .prom files using the Wavelet Prosody Toolkit. Follow the instructions in the Wavelet Prosody Toolkit GitHub repository to generate these files.

Step 2: Convert .prom Files to TextGrid
Once you have the .prom files, you can use the process_files.py script to convert them into TextGrid files.

Command Line Arguments
prom_dir: The directory containing .prom files.
textgrid_dir: The directory containing the corresponding TextGrid files.
out_dir: The output directory where the new TextGrid files will be saved.
Example
Run the script as follows:
```sh
   python process_files.py <prom_dir> <textgrid_dir> <out_dir>
```

Replace <prom_dir>, <textgrid_dir>, and <out_dir> with the appropriate paths.

### Example Directory Structure
```sh
project_root/
├── install_requirements.py
├── process_files.py
├── requirements.txt
├── prom_dir/
│   ├── example1.prom
│   ├── example2.prom
│   └── ...
├── textgrid_dir/
│   ├── example1.TextGrid
│   ├── example2.TextGrid
│   └── ...
└── out_dir/

