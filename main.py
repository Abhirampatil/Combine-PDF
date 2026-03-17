from pypdf import PdfWriter, PdfReader
# pip install pypdf

files = [
    # If the PDF is in the same directory, use just the file name
    "example.pdf",
    
    # If the PDF is inside another folder, use a relative path
    # (e.g., "folder_name/example.pdf")

    # If the PDF is located anywhere on your system, use the absolute path
    # (e.g., "C:/Users/YourName/Documents/example.pdf")
]


writer = PdfWriter()

for file in files:
    reader = PdfReader(file)
    for page in reader.pages:
        writer.add_page(page)
# Specify a valid output file name/path for the merged PDF
output_path = "merged.pdf"

# Write the combined PDF to disk
with open(output_path, "wb") as f:
    writer.write(f)
# output_path contains the location of the final merged PDF
output_path
