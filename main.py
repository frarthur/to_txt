# Filename : main.py
# Author : ratu
# Date : 2020-09-20
# Description : This script converts PDF, DOCX, and ODT files to text files using the PyPDF2, python-docx, and odfpy libraries in Python.

import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install","--user", package])

# List of required packages
required_packages = ["PyPDF2", "python-docx", "odfpy"]

# Install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        install(package)

import PyPDF2
import docx
from odf.opendocument import load
from odf.text import P

def pdf_to_txt(pdf_file_path, txt_file_path):
    try:
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            if pdf_reader.pages:
                with open(txt_file_path, "w", encoding='utf-8') as txt_file:
                    for page in pdf_reader.pages:
                        text = page.extract_text()
                        txt_file.write(text)
            print(f"Conversion of {pdf_file_path} completed successfully.")
            return True
    except Exception as e:
        print(f"An error occurred with {pdf_file_path}: {e}")
        return False

def docx_to_txt(docx_file_path, txt_file_path):
    try:
        doc = docx.Document(docx_file_path)
        with open(txt_file_path, "w", encoding='utf-8') as txt_file:
            for para in doc.paragraphs:
                txt_file.write(para.text + '\n')
        print(f"Conversion of {docx_file_path} completed successfully.")
        return True
    except Exception as e:
        print(f"An error occurred with {docx_file_path}: {e}")
        return False

def odt_to_txt(odt_file_path, txt_file_path):
    try:
        doc = load(odt_file_path)
        with open(txt_file_path, "w", encoding='utf-8') as txt_file:
            for paragraph in doc.getElementsByType(P):
                txt_file.write(paragraph.firstChild.data + '\n')
        print(f"Conversion of {odt_file_path} completed successfully.")
        return True
    except Exception as e:
        print(f"An error occurred with {odt_file_path}: {e}")
        return False

def process_files(in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    files = [f for f in os.listdir(in_folder) if f.endswith(('.pdf', '.docx', '.odt'))]
    successful_conversions = []

    for file in files:
        file_path = os.path.join(in_folder, file)
        txt_file_path = os.path.join(out_folder, file.rsplit('.', 1)[0] + '.txt')
        if file.endswith('.pdf'):
            if pdf_to_txt(file_path, txt_file_path):
                successful_conversions.append(file_path)
        elif file.endswith('.docx'):
            if docx_to_txt(file_path, txt_file_path):
                successful_conversions.append(file_path)
        elif file.endswith('.odt'):
            if odt_to_txt(file_path, txt_file_path):
                successful_conversions.append(file_path)

    if successful_conversions:
        user_input = input("Do you want to delete the successfully converted files from the 'in' folder? (yes/no): ")
        if user_input.lower() in ['yes', 'oui', 'o']:
            for file_path in successful_conversions:
                os.remove(file_path)
            print("Successfully converted files have been deleted.")
        else:
            print("Successfully converted files have been retained.")
    else:
        print("No files were successfully converted.")

# Define the input and output folders
in_folder = "in"
out_folder = "out"

# Process the files
process_files(in_folder, out_folder)