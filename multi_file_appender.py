import os
import sys

def append_files(directory, outfile, target_dir_prefix, target_file_suffix, output_file_suffix):
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            if dirname.startswith(target_dir_prefix):
                for subdirpath, _, subfilenames in os.walk(os.path.join(dirpath, dirname)):
                    for file in sorted(subfilenames):
                        if file.endswith(target_file_suffix):
                            file_path = os.path.join(subdirpath, file)
                            try:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    outfile.write(f'-- Content from {file} --\n')
                                    outfile.write(f.read() + '\n\n')
                            except UnicodeDecodeError:
                                print(f"Error decoding file {file_path}. Skipping.")

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <directory_path> <target_dir_prefix> <target_file_suffix> <output_file_suffix>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    target_dir_prefix = sys.argv[2]
    target_file_suffix = sys.argv[3]
    output_file_suffix = sys.argv[4]
    
    output_file_path = os.path.join(os.getcwd(), f'output_file{output_file_suffix}')
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        append_files(directory_path, outfile, target_dir_prefix, target_file_suffix, output_file_suffix)
    
    print(f"Output written to {output_file_path}")
