from docx import Document

doc = Document('07.docx')
Dictionary = {"." : " ", "," : "", "«" : "", "»" : "", "  " : " "}
for i in Dictionary:
    for p in doc.paragraphs:
        if p.text.find(i)>=0:
            p.text=p.text.replace(i,Dictionary[i])
doc.save('071.docx')