Implementation flow

1.Scraper.py
Description
This Python script performs web scraping on a given search engine URL, searching for
onion links corresponding to specific characters. It uses a list of user agents for variety
and incorporates a 2-second delay between requests to avoid rate limiting. The
discovered onion links are then appended to a text file.
Usage:
Set the search_engine_url variable to the desired search engine URL.
Run the script, and it will iteratively search for onion links corresponding to characters
from a-z, A-Z, 0-9, and special characters.
Dependencies:
Python 3.x
Requests library (pip install requests)

2.run.sh
Description
The provided bash script automates the process of installing and configuring OnionScan,
setting up a Tor proxy using Docker, inspecting the Docker container, and running
OnionScan to scan either a single ".onion" address or multiple addresses from a list.
Usage
In this bash script we download, install, and configure OnionScan, set up a Tor proxy
using Docker, inspect the Docker container, and finally, run OnionScan to scan either a
single ".onion" address or multiple addresses from a list. The results of the scan are then
stored in a text file.
Dependencies
OnionScan:Requires the OnionScan installation script to be downloaded and executed.
Docker:Required for running the Tor proxy container.
OnionScan:Used for scanning ".onion" addresses and generating JSON-formatted
reports.

3.search_for_hidden.py
Description:
Takes .txt as input generated from run.sh and runs scripts to find all
linked URLs from the enumerated URLs we get from Onion Scan.
These linked URLs are further classified as v2 or v3 URLs based on
their length (16 bit or 56 bit respectively).
Thus, URLs are enumerated.
Further we also check if the URLs found are publicly available or not by comparing the
linked URLs to a list of publicly available URLs.
