import pdfplumber
import json
import os
import glob
import time

# Get a list of all PDF files in the current directory
pdf_files = glob.glob('*.pdf')

# If no PDF files are found, print an error message and exit
if not pdf_files:
    print("Error: No PDF files found in the current directory.", flush=True)
    exit()

# Process each PDF file
for filename in pdf_files:
    # Remove the .pdf extension for the output filename
    output_filename = os.path.splitext(filename)[0]

    print(f"Processing {filename}...", flush=True)

    # Start timing
    start_time = time.time()

    # Open the PDF
    with pdfplumber.open(filename) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            # Some pages might not have text, so we ensure not to append None
            if page_text:
                text += page_text

    # Split the text into chunks
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

    # Save the chunks to a JSON file
    with open(f'{output_filename}.json', 'w') as f:
        json.dump(chunks, f)

    # Calculate and print processing time
    processing_time = int(time.time() - start_time)

    print(f"Finished processing {filename} in {processing_time} seconds. {len(chunks)} chunks created. Output saved to {output_filename}.json.", flush=True)
