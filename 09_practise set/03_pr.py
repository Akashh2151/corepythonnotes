for i in range(2,21):
    with open(f"xxx.txt{i}",'w') as f:
        for j in range(1,11):
            print(f"{i}x{j}={i*j}\n")
        if j!=10:
            f.write('\n')