import os
import re
import urllib.request as ul
from urllib.parse import urlparse

def check_file(name: str):
    """
    Checks whether a file with the given name exists in the 'downloaded_pdfs' folder.

    Args:
        name (str): Name of the file to check.

    Returns:
        bool: True if the file does not exist, False otherwise.
    """
    if name not in os.listdir("downloaded_pdfs"):
        return True
    else:
        print(f"File {name} already exists")
        return False

def extract_base_url(url):
    """
    Extracts the base URL from a given URL.

    Args:
        url (str): The URL to extract the base from.

    Returns:
        str: The base URL (scheme and netloc).
    """
    try:
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return base_url
    except Exception as e:
        print(f"Something went wrong while parsing the URL: {e}\n")

def load_links(file_name: str):
    """
    Loads a list of links from a text file.

    Args:
        file_name (str): Name of the file containing the links.

    Returns:
        list: A list of URLs read from the file, or an empty list if an error occurs.
    """
    try:
        with open(file_name, "r") as file:
            data = file.read().split()
            return data
    except Exception as e:
        print(f"Something went wrong while trying to load links: {e}")
        return []

def pdf_target(url: str, out_file=0):
    """
    Downloads a PDF file from the given URL and saves it to the 'downloaded_pdfs' folder.

    Args:
        url (str): The URL of the PDF file.
        out_file (str, optional): Name of the output file. Defaults to 0 (uses the last part of the URL).
    """
    try:
        if not out_file:
            print("No output file given, storing the file as: ", end="")
            out_file = url.split("/")[-1]
            print(out_file)
        out_file = os.curdir + "/downloaded_pdfs/" + str(out_file)
        
        if check_file(out_file):
            output = ul.urlopen(url)
            with open(out_file, "wb") as file:
                file.write(output.read())
        else:
            print(f"{out_file} already exits")

    except Exception as e:
        print(f"Unable to download the file due to {e}")

def ebook_target(url: str, out_file=0):
    """
    Extracts the PDF link from an ebook page, then downloads the PDF.

    Args:
        url (str): The URL of the ebook page.
        out_file (str, optional): Name of the output file. Defaults to 0 (uses the last part of the URL).
    """
    try:
        url_data = ul.urlopen(url).read().decode("utf-8")
        pattern = r"/[a-zA-Z]*/([^/]+\.pdf)"
        print(url)
        x = re.search(pattern, url_data).group(0)
        if not out_file:
            out_file = url.split("/")[-1]
        final_url = extract_base_url(url) + x
        pdf_target(final_url, out_file)
    except AttributeError:
        print(f"Unable to download the file as the URL {url} doesn't contain a valid file")
    except Exception as e:
        print(f"Unable to download the file due to {e}")

def extract_id(url):
    """
    Extracts an ID parameter from a URL.

    Args:
        url (str): The URL containing the ID.

    Returns:
        str: The extracted ID, or None if not found.
    """
    try:
        pattern = r"id=[^?|#]*"
        return re.search(pattern, url).group(0)[3:]
    except Exception as e:
        print(f"Unable to extract ID due to {e}")

def id_target(url: str):
    """
    Constructs an ebook URL from an extracted ID and downloads the corresponding PDF.

    Args:
        url (str): The URL containing the ID parameter.
    """
    id = extract_id(url)
    template = f"https://www.ebharatisampat.in/ebook/index.php?bookid={id}#book/"
    ebook_target(template)

def downloads_folder():
    """
    Ensures that the 'downloaded_pdfs' folder exists, creating it if necessary.
    """
    if "downloaded_pdfs" not in os.listdir():
        print("\nNo folder found for downloaded PDFs, creating a new folder.....")
        os.mkdir("downloaded_pdfs")
        print("Created a new folder 'downloaded_pdfs'.")
    else:
        print("Found folder for downloaded_pdfs")

if __name__ == "__main__":
    """
    Main script logic to load links, ensure the downloads folder exists, and process each link to download PDFs.
    """
    links = load_links("Links.txt")
    downloads_folder()

    for i, file in enumerate(links):
        print(f"\nProcessing link {i+1}:")
        if "id=" in file:
            id_target(file)
        elif ".pdf" in file:
            pdf_target(file)
        elif "ebook" in file:
            ebook_target(file)
        else:
            print("Something went wrong! Please verify the links.")

