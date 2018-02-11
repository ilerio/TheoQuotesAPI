from magic import get_text
txt = get_text()
file = open("file.txt","w")
file.write(txt)
file.close()
