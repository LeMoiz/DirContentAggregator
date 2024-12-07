import os
import sys

def append_files(directory, outfile, target_dir_prefix, target_file_suffix):
    for dirpath, dirnames, filenames in os.walk(directory):
        # If target_dir_prefix is specified, filter to only those sub-directories
        if target_dir_prefix:
            dirnames[:] = [d for d in dirnames if d.startswith(target_dir_prefix)]
            # Skip files in the root directory
            if dirpath == directory:
                continue
        
        # Process files in the current directory (if prefix is None or within subdirectory)
        for file in sorted(filenames):
            if not target_file_suffix or file.endswith(target_file_suffix):
                file_path = os.path.join(dirpath, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        outfile.write(f.read() + '\n\n')
                except UnicodeDecodeError:
                    print(f"Error decoding file {file_path}. Skipping.")

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <directory_path> <target_dir_prefix> <target_file_suffix> <output_file_suffix>")
        sys.exit(1)

    directory_path = sys.argv[1]
    target_dir_prefix = None if sys.argv[2] == "None" else sys.argv[2]
    target_file_suffix = None if sys.argv[3] == "None" else sys.argv[3]
    output_file_suffix = sys.argv[4]
    
    output_file_path = os.path.join(os.getcwd(), f'output_file{output_file_suffix}')
    
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        append_files(directory_path, outfile, target_dir_prefix, target_file_suffix)
    
    print(f"Output written to {output_file_path}")
