from docx import Document
from docx.shared import Pt
import re
#Copy of Sources Sought Synopsis Manuals 8 Jan 2020
#02 - DRAFT_6_SUAS_Engineering_Services_Sample_TO_08Nov19 (Task Order 0
document2 = Document("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")


runtext = []
boldingFound = False
breakOut = False
for perry in document2.paragraphs:
    if(breakOut):
        break
    for rooms in perry.runs:
        if(boldingFound == False):
            requirementSearch = re.findall("Requirements", rooms.text)
            if(len(requirementSearch) >= 1 and rooms.bold):
                runtext.append(rooms.text)
                boldingFound = True
        else:
            if(rooms.bold):
                breakOut = True
                break
            else:
                runtext.append(rooms.text)
        
        
print(runtext)


'''
underHeading = False
for par in document2.paragraphs:
    if (underHeading == True):
        print(par.text + "\n")
        underHeading = False
    if (par.style.name.startswith('Heading') ):
        underHeading = True


make it so that until next heading grab all the info
search for headings with our keywords
'''

# code is pretty simple but there are many issues that are headaches:
# some documents have alot of headings that are random/ not needed
# making a list of headings that are acceptable and checking them might help, but it also restricts how useful the program is
# (any doc without any of those headings would not have a summary )
# in some documents there is and empty section between the heading and the next text block, while in others it is right after
