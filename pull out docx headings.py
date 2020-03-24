from docx import Document
document2 = Document("Test.docx")


for par in document2.paragraphs:
    if(par.style.name.startswith('Heading')):
        print(par.text)
