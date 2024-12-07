# Multi File Appender

This Python script traverses a directory structure, filtering directories and files based on specified conditions, and appends the content of matching files into a single output file. It is useful for combining scripts or text files stored in a nested folder structure.

## Features
- Filters directories that start with a specified string (`startswith_filter`).
- Filters files that end with a specified string (`endswith_filter`).
- Default filters:
  - Directories starting with `V`.
  - Files ending with `.sql`.
- Supports aggregating content from any file type (e.g., `.txt`, `.log`, `.py`).
- Outputs aggregated content into a single `output_file.sql` in the current working directory.
- Handles `UnicodeDecodeError` gracefully by skipping problematic files.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Command-Line Usage
```bash
python script.py <directory_path> [startswith_filter] [endswith_filter]
```

### Parameters
1. `directory_path` (required): The root directory to start searching.
2. `startswith_filter` (optional): Filters directories that start with this string. Default is `V`. Use `None` to skip this filter.
3. `endswith_filter` (optional): Filters files that end with this string. Default is `.sql`. Use `None` to skip this filter.

### Example Commands
- Aggregate `.sql` files in directories starting with `V`:
  ```bash
  python script.py /path/to/root
  ```

- Aggregate `.txt` files in directories starting with `S`:
  ```bash
  python script.py /path/to/root S .txt
  ```

- Aggregate all files, ignoring filters:
  ```bash
  python script.py /path/to/root None None
  ```

- Aggregate `.log` files in all directories:
  ```bash
  python script.py /path/to/root None .log
  ```

## Output
The script creates a file named `output_file.sql` in the current working directory, containing the aggregated content of all matched files.

## Error Handling
- Files that cannot be read due to encoding issues are skipped, and an error message is printed.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests to enhance this script!

## Author
[LeMoiz](https://github.com/LeMoiz)
**
