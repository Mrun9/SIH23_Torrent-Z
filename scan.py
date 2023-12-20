import os
import json

def find_text_in_json_files(folder_path, keyword):
    """
    Iterates over JSON files in a folder, searches for text containing a keyword, and prints the relevant text.

    Args:
        folder_path: The path to the folder containing the JSON files.
        keyword: The keyword to search for within the text of the JSON files.

    Returns:
        Tuple: A tuple containing the counts of files found and not found.
    """
    files_found = 0
    files_not_found = 0
    files_with_errors = []

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath) and filepath.endswith(".json"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Find text containing the keyword within the JSON data
                found_text = None
                for item in data.values():
                    if isinstance(item, (str, list)):
                        if keyword in item:
                            found_text = item
                            break

                # Print the relevant text or an indication if not found
                print(f"File: {filename}")
                if found_text is not None:
                    print(f"Found text containing '{keyword}': {found_text}")
                    files_found += 1
                else:
                    print(f"Keyword '{keyword}' not found")
                    files_not_found += 1

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {filename}: {e}")
                files_with_errors.append(filename)
            except UnicodeDecodeError as e:
                print(f"Unicode decoding error in file {filename}: {e}")
                files_with_errors.append(filename)

    if files_with_errors:
        print("\nFiles with errors:")
        for error_file in files_with_errors:
            print(f"- {error_file}")

    return files_found, files_not_found

# Example usage
folder_path = "C:/Users/HP/Documents/Projects/OnionScan/onionscan_results"
keyword = "foundApacheModStatus"

files_found, files_not_found = find_text_in_json_files(folder_path, keyword)

print("Files found:", files_found)
print("Files not found:", files_not_found)
