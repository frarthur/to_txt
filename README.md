# File to Text Converter

This project converts PDF, DOCX, ODT, and Excel files (both `.xlsx` and `.ods` formats) to text files using Python. It processes all files in a specified input folder and saves the extracted text to a specified output folder.

## Prerequisites

- Python 3.x
- The required libraries will be installed automatically when the script is executed.

## Installation

1. Clone the repository or [download](https://codeload.github.com/frarthur/to_txt/zip/refs/heads/main) the source code.

## Usage

1. Place the files you want to convert in the `in` folder.
Windows :
2. Run the run.bat script:

macOS / Linux :
2. Run the `run.sh` script:

    ```sh
    chmod +x run.sh
    run.sh
    ```

3. The extracted text files will be saved in the `out` folder.
4. After the conversion, you will be prompted to delete the successfully converted PDF files from the `in` folder. You can respond with `yes`, `oui`, or `o` to delete the files, or any other input to retain them.

## Project Structure
- `in/`: Folder containing the PDF files to be converted.
- `main.py`: Main script to convert PDF files to text files.
- `out/`: Folder where the converted text files will be saved.

## Functions

### `pdf_to_txt(pdf_file_path, txt_file_path)`

Converts a single PDF file to a text file.

- `pdf_file_path`: Path to the PDF file.
- `txt_file_path`: Path to save the extracted text file.

### `docx_to_txt(docx_file_path, txt_file_path)`

Converts a single DOCX file to a text file.

- `docx_file_path`: Path to the DOCX file.
- `txt_file_path`: Path to save the extracted text file.

### `odt_to_txt(odt_file_path, txt_file_path)`

Converts a single ODT file to a text file.

- `odt_file_path`: Path to the ODT file.
- `txt_file_path`: Path to save the extracted text file.

### `excel_to_txt(excel_file_path, txt_file_path)`

Converts a single Excel file (both `.xlsx` and `.ods` formats) to a text file.

- `excel_file_path`: Path to the Excel file.
- `txt_file_path`: Path to save the extracted text file.

### `process_files(in_folder, out_folder)`

Processes all PDF, DOCX, ODT, and Excel files in the input folder and converts them to text files in the output folder.

- `in_folder`: Path to the input folder containing files.
- `out_folder`: Path to the output folder to save the text files.