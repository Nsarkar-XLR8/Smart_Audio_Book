'''
 Writing Code For Smart Audio Book


 Writing Comment For Each Line Becasue The module "PyPDF" verision keeps getting updated.

This Code is in Version 3.0.0 (So, everybody can understand easily)
'''


import pyttsx3
import fitz  # PyMuPDF

# Open the PDF file
book = open('OOP_Python.pdf', 'rb')
pdfReader = fitz.open(book)  # Use PyMuPDF to open the PDF
no_of_pages = pdfReader.page_count  # Get the number of pages in the PDF
print(no_of_pages)

friend = pyttsx3.init()  # Initialize the text-to-speech engine

# Iterate through pages 7 to 110
for page_number in range(7, 111):
    page = pdfReader[page_number]  # Get a specific page
    text = page.get_text()  # Extract text from the page
    friend.say(text)  # Use pyttsx3 to say the extracted text

friend.runAndWait()  # Wait for the text-to-speech engine to finish

book.close()  # Close the PDF file

