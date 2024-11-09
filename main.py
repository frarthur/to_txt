import os
import PyPDF2

def pdf_to_txt(pdf_file_path, txt_file_path):
    try:
        # Open the PDF file in binary mode
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # Check the pages of the PDF
            if pdf_reader.pages:
                # Create a text file to save the extracted text
                with open(txt_file_path, "w", encoding='utf-8') as txt_file:
                    # Loop through each page of the PDF
                    for page in pdf_reader.pages:
                        # Extract the text from the page
                        text = page.extract_text()
                        # Write the extracted text to the text file
                        txt_file.write(text)
            print(f"Conversion of {pdf_file_path} completed successfully.")
            return True
    except Exception as e:
        print(f"An error occurred with {pdf_file_path}: {e}")
        return False

def process_pdfs(in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    pdf_files = [f for f in os.listdir(in_folder) if f.endswith('.pdf')]
    successful_conversions = []

    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(in_folder, pdf_file)
        txt_file_path = os.path.join(out_folder, pdf_file.replace('.pdf', '.txt'))
        if pdf_to_txt(pdf_file_path, txt_file_path):
            successful_conversions.append(pdf_file_path)

    if successful_conversions:
        user_input = input("Do you want to delete the successfully converted PDF files from the 'in' folder? (yes/no): ")
        if user_input.lower() in ['yes', 'oui', 'o']:
            for pdf_file_path in successful_conversions:
                os.remove(pdf_file_path)
            print("Successfully converted PDF files have been deleted.")
        else:
            print("Successfully converted PDF files have been retained.")
    else:
        print("No PDF files were successfully converted.")

# Define the input and output folders
in_folder = "in"
out_folder = "out"

# Process the PDFs
process_pdfs(in_folder, out_folder)