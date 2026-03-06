f1 = open("source.txt", "r")
f2 = open("copy.txt", "w")
for line in f1:
    f2.write(line)
print("File copied successfully")
f1.close()
f2.close()
