import os
import re

def check_urls(database_path, tosearch_path):
    """Checks for URLs in tosearch file present in the database file."""

    public_urls = []
    hidden_urls = []

    # Ensure file paths are correct and files exist
    if not os.path.isfile(database_path):
        raise FileNotFoundError(f"Database file not found: {database_path}")
    if not os.path.isfile(tosearch_path):
        raise FileNotFoundError(f"Tosearch file not found: {tosearch_path}")

    with open(database_path, 'r') as database_file:
        database_urls = set(line.strip() for line in database_file)

    with open(tosearch_path, 'r') as tosearch_file:
        for url in tosearch_file:
            # Remove only leading whitespaces
            url = url.strip()
            if url in database_urls:
                public_urls.append(url)
            else:
                hidden_urls.append(url)

    return public_urls, hidden_urls

def extract_linked_onions(input_filename, output_filename_v2, output_filename_v3, length_threshold=30):
    """Extracts unique "linkedOnions" values, categorizing URLs based on length, and counts websites, saving onions to files."""

    seen_onions_v2 = set()  # Keeps track of unique onions with length <= length_threshold
    seen_onions_v3 = set()  # Keeps track of unique onions with length > length_threshold
    website_count = 0  # Counts total websites

    with open(input_filename, 'r') as input_file, open(output_filename_v2, 'w') as output_file_v2, open(output_filename_v3, 'w') as output_file_v3:
        for line in input_file:
            # Count websites (assuming identified by URL format)
            website_match = re.findall(r"https?://[^\s]+", line)
            website_count += len(website_match)

            # Extract and process "linkedOnions"
            match = re.search(r'"linkedOnions":\s*\[(.*?)\]', line)
            if match:
                onions = match.group(1).strip()  # Remove extra spaces
                onions = onions.replace('"', '')  # Remove double quotes
                for onion in onions.split(','):
                    onion = onion.strip()
                    if len(onion) <= length_threshold:
                        if onion not in seen_onions_v2:  # Check if onion is unique for v2
                            seen_onions_v2.add(onion)
                            output_file_v2.write(onion + '\n')
                    else:
                        if onion not in seen_onions_v3:  # Check if onion is unique for v3
                            seen_onions_v3.add(onion)
                            output_file_v3.write(onion + '\n')

    # Print results after processing the entire file
    print(f"Number of websites pasted: {website_count}")
    print(f"Number of unique onions in v2 (length <= {length_threshold}): {len(seen_onions_v2)}")
    print(f"Number of unique onions in v3 (length > {length_threshold}): {len(seen_onions_v3)}")



# Example usage:
input_filename = 'hs.txt'
output_filename_v2 = 'extracted_onions_v2.txt'
output_filename_v3 = 'extracted_onions_v3.txt'
extract_linked_onions(input_filename, output_filename_v2, output_filename_v3, length_threshold=30)

database_path = "all.txt"
#tosearch_path = "extracted_onions_v3.txt"
public_urls, hidden_urls = check_urls(database_path, output_filename_v3)

print("Public URLs:")
for url in public_urls:
    print(url)

print("\nHidden URLs:")
for url in hidden_urls:
    print(url)

print("number of public URLs found = ",len(public_urls))
print("number of hidden URLs found = ",len(hidden_urls))