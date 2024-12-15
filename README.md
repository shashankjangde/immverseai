# 📄 Automated PDF Downloader 🚀

Welcome to the **Automated PDF Downloader**! This Python-based tool simplifies downloading PDF files from various types of links, so you can save time and focus on what matters most. 🖥️
---

## ⚙️ Demo of the Project

### 1. Running the Scraper:
![1](https://github.com/user-attachments/assets/f77ae22d-3724-4df5-b112-ec649fd3ff94)

### 2. Viewing the Downloaded files:
![New Project](https://github.com/user-attachments/assets/2d46a3a3-9b7f-4564-95ff-2bd9db546975)

---

## ✨ Features

- **Direct PDF Downloads**: Handles URLs linking directly to PDF files.  
- **Ebook PDF Extraction**: Extracts and downloads PDFs from ebook pages.  
- **ID-based PDF Links**: Detects and constructs URLs for PDF resources using embedded IDs.  
- **Automatic Folder Creation**: Ensures a dedicated folder for downloaded PDFs.  
- **Duplicate Avoidance**: Skips downloading files that already exist.  

---

## ⚙️ Setup and Usage Instructions

### Step 1: Prerequisites

1. **Python Installation**  
   Ensure Python (version 3.6 or higher) is installed. [Download Python here](https://www.python.org/).

2. **Required Libraries**  
   The project utilizes the following libraries:
   - `os` (pre-installed with Python)
   - `re` (pre-installed with Python)
   - `urllib` (pre-installed with Python)  
   For advanced URL handling, install `urllib3`:
   ```bash
   pip install urllib3
   ```

---

### Step 2: Setting Up the Project

1. **Download the Code**  
   Save the script (`download_pdfs.py`) to your desired folder.

2. **Prepare the Links File**  
   - Create a `Links.txt` file in the same directory as the script.
   - Populate `Links.txt` with one URL per line (e.g., direct PDF links, ebook pages, or ID-based links).

3. **Output Folder**  
   The script will automatically create a folder named `downloaded_pdfs` to store downloaded files.

---

### Step 3: Running the Script

1. **Navigate to the Project Folder**  
   Open a terminal or command prompt and navigate to the script's directory:
   ```bash
   cd /path/to/project
   ```

2. **Run the Script**  
   Execute the script:
   ```bash
   python download_pdfs.py
   ```

3. **Monitor Progress**  
   - The script reads URLs from `Links.txt` and processes them sequentially.  
   - Downloaded files are saved in the `downloaded_pdfs` folder.  
   - Duplicate files are skipped automatically.

---

### Step 4: Troubleshooting 🛠️

- **Invalid Links**: If a URL is invalid or a file cannot be extracted, an error message will be printed.  
- **Folder Not Found**: The script creates the `downloaded_pdfs` folder automatically if it doesn't exist.  
- **Script Permissions**: Ensure the script has write permissions in the current directory.

---

## 🧑‍💻 Code Overview

Here’s a glance at the core functionality of the script:

- **Download Handling**: The script uses `urllib` to fetch and save files.  
- **Dynamic URL Processing**: Handles URLs for ebooks and ID-based resources using regex.  
- **File Management**: Prevents overwriting existing files by checking their presence.

### Example Functions

- **`pdf_target(url)`**  
  Downloads a PDF from a direct link.  
- **`ebook_target(url)`**  
  Extracts and downloads a PDF from an ebook page.  
- **`id_target(url)`**  
  Constructs an ebook URL using an ID and downloads the associated PDF.  

For more details, explore the complete script in the code section.

---

## 📂 Folder Structure

```
project/
├── download_pdfs.py   # Main script
├── Links.txt          # Input file for URLs
└── downloaded_pdfs/   # Folder for downloaded PDFs
```
