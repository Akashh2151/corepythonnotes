import os

old_file="xxx.txt7"
new_file="x1.txt"

with open('x1.txt') as f1:
    content=f1.read()

with open('xxx.txt7','w') as f2:
    f2.write(content)


os.remove('x1.txt')    