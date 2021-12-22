#!C:\Python38\python.exe
print "Content-type: text/html\n\nm

form = cgi.FieldStorage()

fileitem = form["filename"]

if fileitem.filename:
 fn = os.path.basename(fileitem.filename)
 open(fn,'wb').write(fileitem.file.read())
 
 message = 'el archivo fue cargado'
 print message

else:
 message = 'el archivo no fue cargado'
 print message









