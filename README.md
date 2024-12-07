# Multi File Appender

This Python script aggregates the contents of files from a directory structure based on user-defined directory and file naming patterns. It outputs the combined content to a single file, providing flexibility in content organization and aggregation.

## Features
- **Directory Filtering**: Process directories starting with a specified prefix (e.g., `V`).
- **File Filtering**: Include files ending with a specified suffix (e.g., `.sql`).
- **Customizable Output File**: Specify the extension of the output file (e.g., `.txt`, `.sql`).
- **Error Handling**: Skips files that cannot be read due to encoding issues (`UnicodeDecodeError`).

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Command-Line Usage
```bash
python script.py <directory_path> <target_dir_prefix> <target_file_suffix> <output_file_suffix>
```

### Parameters
1. **`directory_path`** (required): Root directory to start searching.
2. **`target_dir_prefix`** (required): Filters directories starting with this string (e.g., `V`). Use `None` to skip this filter.
3. **`target_file_suffix`** (required): Filters files ending with this string (e.g., `.sql`). Use `None` to skip this filter.
4. **`output_file_suffix`** (required): Extension for the output file (e.g., `.txt`).

### Example Commands
- **Aggregate `.sql` files in directories starting with `V`:**
  ```bash
  python script.py /path/to/root V .sql .txt
  ```

- **Aggregate `.txt` files in directories starting with `S`:**
  ```bash
  python script.py /path/to/root S .txt .log
  ```

- **Aggregate all files, ignoring filters:**
  ```bash
  python script.py /path/to/root None None .out
  ```

- **Aggregate `.log` files in all directories:**
  ```bash
  python script.py /path/to/root None .log .log
  ```

## Output
The script creates an output file named `output_file.<output_file_suffix>` in the current working directory. This file contains the aggregated content of all matched files, with each file's content prefixed by a header indicating its source.

## Error Handling
- Files that cannot be read due to encoding issues are skipped with a warning.

## License
This project is licensed under the MIT License.

## Contributing
Contributions, issues, and pull requests are welcome to enhance this script!

## Author
[LeMoiz](https://github.com/LeMoiz)
