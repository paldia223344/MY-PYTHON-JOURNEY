# word = "donkey"
# with open(r"CHAPTER-9 FILE I\O\filr.txt","r")as f:
#      content = f.read
     
# result = content.replace("word","#####")
     
# with open(r"CHAPTER-9 FILE I\O\filr.txt","w")as f:
#     f.write(result)
    
import re

word = "donkey"

with open(r"C:\Users\Ravi\Desktop\PYTHON\CHAPTER-9 FILE I\filr.txt", "r") as f:
    content = f.read()

# Replace all case variations of "donkey"
result = re.sub(word, "#####", content, flags=re.IGNORECASE)

with open(r"C:\Users\Ravi\Desktop\PYTHON\CHAPTER-9 FILE I\filr.txt", "w") as f:
    f.write(result)

# Verify
with open(r"C:\Users\Ravi\Desktop\PYTHON\CHAPTER-9 FILE I\filr.txt", "r") as f:
    print(f.read())