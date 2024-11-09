# PDF to Text Converter

This project converts PDF files to text files using Python. It processes all PDF files in a specified input folder and saves the extracted text to a specified output folder.

## Prerequisites

- Python 3.x
- The required libraries will be installed automatically when the script is executed.

## Installation

1. Clone the repository or [download](https://codeload.github.com/frarthur/to_txt/zip/refs/heads/main) the source code.

## Usage

1. Place the PDF files you want to convert in the `in` folder.
2. Run the `main.py` script:

    ```sh
    python main.py
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

### `process_pdfs(in_folder, out_folder)`

Processes all PDF files in the input folder and converts them to text files in the output folder.

- `in_folder`: Path to the input folder containing PDF files.
- `out_folder`: Path to the output folder to save the text files.

## Example

Windows :
Place your PDF, DOCX, and ODT files in the `in` folder and run run.bat

macOS / Linux :
Place your PDF, DOCX, and ODT files in the `in` folder and open a terminal. Navigate to the directory containing `run.sh`, <span title="type chmod +x run.sh.">make it executable</span> if it is not already, and then execute it:

```sh
chmod +x run.sh
<<<<<<< HEAD
run.sh
=======
run.sh
>>>>>>> 4bb6a6604d754273dc9440841e549d05a9550fe0
