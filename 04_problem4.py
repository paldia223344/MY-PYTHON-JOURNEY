word = "donkey"
with open(r"CHAPTER-9 FILE I\O\filr.txt","r")as f:
     content = f.read
     
result = content.replace("word","#####")
     
with open(r"CHAPTER-9 FILE I\O\filr.txt","w")as f:
    f.write(result)
    
