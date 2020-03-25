from docx import Document

document2 = Document("test1.docx")

underHeading = False
for par in document2.paragraphs:
    if (underHeading == True):
        print(par.text)
        underHeading = False
    if (par.style.name.startswith('Heading') ):
        underHeading = True



# code is pretty simple but there are many issues that are headaches:
# some documents have alot of headings that are random/ not needed
# making a list of headings that are acceptable and checking them might help, but it also restricts how useful the program is
# (any doc without any of those headings would not have a summary )
# in some documents there is and empty section between the heading and the next text block, while in others it is right after
