# JSON to JSONL Converter

A simple Python script that reads all JSON files from a folder and combines them into a single JSONL (JSON Lines) file.

## Features

- 🔍 Automatically finds all `.json` files in a specified folder
- 📄 Handles different JSON structures (objects, arrays, primitives)
- 🛡️ Robust error handling for malformed JSON files
- 🌍 Full Unicode support with UTF-8 encoding
- ⚡ Simple command-line interface

## Installation

No additional dependencies required - uses only Python standard library.

```bash
git clone <repository-url>
cd json-to-jsonl-converter
```

## Usage

```bash
python json_to_jsonl.py <folder_name>
```

### Examples

```bash
# Convert all JSON files in 'data' folder to 'data.jsonl'
python json_to_jsonl.py data

# Convert all JSON files in 'json_files' folder to 'json_files.jsonl'
python json_to_jsonl.py json_files
```

## How it works

The script processes JSON files based on their structure:

- **Single JSON object**: Written as one line in the JSONL file
- **JSON array**: Each array element becomes a separate line
- **Other types**: Written as-is on a single line

## Output Format

The output follows the [JSON Lines](https://jsonlines.org/) format, where each line is a valid JSON object:

```jsonl
{"name": "John", "age": 30}
{"name": "Jane", "age": 25}
{"name": "Bob", "age": 35}
```

## Error Handling

The script gracefully handles:
- Non-existent folders
- Invalid JSON files
- File permission issues
- Empty folders

Errors are reported to the console while processing continues for valid files.

## Requirements

- Python 3.6 or higher

## License

MIT License - feel free to use and modify as needed.
