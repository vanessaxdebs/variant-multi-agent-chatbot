"""
Download raw HumSavar dataset automatically.
"""

import requests
import os

def download_humsavar():
    url = "https://www.uniprot.org/docs/humsavar.txt"
    output_path = "../data/raw/humsavar.txt"

    # Make sure raw folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Download file
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded HumSavar to {output_path}")
    else:
        print(f"Failed to download. Status code: {response.status_code}")

if __name__ == "__main__":
    download_humsavar()
