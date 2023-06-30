file1='06_pr.txt'
file2='xxx.txt7'

with open(file1) as f:
    f1=f.read()

with open(file2) as f:
    f2=f.read()

if f1 == f2:
    print("file are identical")
else:
    print("file not identical")    
