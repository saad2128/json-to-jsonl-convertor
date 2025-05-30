import json
import os
from pathlib import Path

def json_files_to_jsonl(input_folder, output_file="output.jsonl"):
    """
    Read all JSON files from a folder and combine them into a JSONL file.
    
    Args:
        input_folder (str): Path to folder containing JSON files
        output_file (str): Output JSONL file path
    """
    input_path = Path(input_folder)
    
    # Check if input folder exists
    if not input_path.exists():
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return
    
    if not input_path.is_dir():
        print(f"Error: '{input_folder}' is not a directory.")
        return
    
    # Find all JSON files
    json_files = list(input_path.glob("*.json"))
    
    if not json_files:
        print(f"No JSON files found in '{input_folder}'")
        return
    
    print(f"Found {len(json_files)} JSON files")
    
    # Process files and write to JSONL
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as infile:
                    data = json.load(infile)
                    
                    # If the JSON contains a single object, write it as one line
                    if isinstance(data, dict):
                        json.dump(data, outfile, ensure_ascii=False)
                        outfile.write('\n')
                    
                    # If the JSON contains a list, write each item as a separate line
                    elif isinstance(data, list):
                        for item in data:
                            json.dump(item, outfile, ensure_ascii=False)
                            outfile.write('\n')
                    
                    # For other types, write as-is
                    else:
                        json.dump(data, outfile, ensure_ascii=False)
                        outfile.write('\n')
                        
                print(f"Processed: {json_file.name}")
                
            except json.JSONDecodeError as e:
                print(f"Error reading {json_file.name}: Invalid JSON - {e}")
            except Exception as e:
                print(f"Error processing {json_file.name}: {e}")
    
    print(f"JSONL file created: {output_file}")

def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_name>")
        print("Example: python script.py data_folder")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_file = f"{input_folder}.jsonl"
    
    json_files_to_jsonl(input_folder, output_file)

if __name__ == "__main__":
    main()
