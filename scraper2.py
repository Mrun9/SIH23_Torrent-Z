import os
import requests
import random
import re
import time
def Scraper(search_engine_url):
    print(f"Starting scraping for {search_engine_url}")

    def findlinks(content):
        regexquery = "\w+\.onion"
        mineddata = re.findall(regexquery, content)
        mineddata = list(dict.fromkeys(mineddata))

        filename = "g.txt"

        with open(filename, "a+") as file:
            file.seek(0)
            existing_links = file.read().splitlines()

            for link in mineddata:
                if link not in existing_links:
                    file.write(link + "\n")

        print("All the files written to a text file: ", filename)

    # Arrays for characters
    lowercase_letters = [chr(char) for char in range(ord('a'), ord('z') + 1)]
    uppercase_letters = [chr(char) for char in range(ord('A'), ord('Z') + 1)]
    digits = [str(digit) for digit in range(0, 10)]
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', '{', '}', '[', ']', ';', ':', ',', '<', '>', '.', '?', '/']

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Loop for all characters
    for yourquery in all_characters:
        url = f"{search_engine_url}?q={yourquery}"
        make_request(url, yourquery, findlinks)

def make_request(url, yourquery, findlinks_function):


    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
        "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
        # Add more user agents as needed
    ]

    ua = random.choice(ua_list)
    headers = {'User-Agent': ua}
    time.sleep(2)  # Add a delay of 2 seconds (adjust as needed)
    request = requests.get(url, headers=headers)

    if request.status_code == 200:
        print(f"Query: {yourquery} - Request went through.")
        content = request.text
        findlinks_function(content)
    else:
        print(f"Query: {yourquery} - Request failed with status code {request.status_code}.")

# Example usage for Ahmia

torsearch_url="https://torsearch.com/search"
# Example usage for another search engine
# Replace "https://example_search_engine.onion/" with the URL of the search engine you want to use
Scraper(torsearch_url)