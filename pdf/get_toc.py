import PyPDF2

# Open the PDF file
pdf_file = PyPDF2.PdfReader(
    open('./CIS_Ubuntu_Linux_22.04_LTS_Benchmark_v1.0.0.pdf', 'rb'))

# Check if the PDF has a table of contents
if pdf_file.outline:
    outlines = pdf_file.outline

    # Print the table of contents
    for (level, title, dest, a, se) in outlines:
        print('Level:', level)
        print('Title:', title)
        print('Destination:', dest)
        print('------------------')
else:
    print('No table of contents found')
