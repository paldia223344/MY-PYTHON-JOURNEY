words= ["denkey","key"]
with open("CHAPTER-9 FILE I\\filr.txt","r")as f:
    content = f.read()
    
for word in words:
    content = content.replace(word,"#" * len(word))
    
with open("CHAPTER-9 FILE I\\filr.txt","w")as f:
    f.write(content)