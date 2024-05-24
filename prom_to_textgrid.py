import os
import textgrid
import argparse

def process_files(prom_dir, textgrid_dir, out_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    for file in os.listdir(prom_dir):
        if file.endswith(".prom"):
            print(file.split('.')[0])
            tg_file = os.path.splitext(file)[0] + '.TextGrid'  
            tg_path = os.path.join(textgrid_dir, tg_file)

            with open(os.path.join(prom_dir, file), 'r') as prom_file:
                data = [line.strip().split('\t') for line in prom_file]

            tg = textgrid.TextGrid.fromFile(tg_path)

            tier1 = textgrid.IntervalTier(name="prominence strength")
            tier2 = textgrid.IntervalTier(name="boundary strength")

            for entry in data:
                start_time = float(entry[1])
                end_time = float(entry[2])
                prominence = entry[4]
                boundary = entry[5]

                tier1.add(start_time, end_time, prominence)
                tier2.add(start_time, end_time, boundary)

            tg.append(tier1)
            tg.append(tier2)

            new_tg_path = os.path.join(out_dir, tg_file)

            with open(new_tg_path, "w", encoding="utf-8") as f:
                tg.write(f)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process .prom files and corresponding TextGrid files.')
    parser.add_argument('prom_dir', type=str, help='The directory containing .prom files')
    parser.add_argument('textgrid_dir', type=str, help='The directory containing TextGrid files')
    parser.add_argument('out_dir', type=str, help='The output directory')
    
    args = parser.parse_args()
    
    # Call the processing function with the provided arguments
    process_files(args.prom_dir, args.textgrid_dir, args.out_dir)

if __name__ == "__main__":
    main()
