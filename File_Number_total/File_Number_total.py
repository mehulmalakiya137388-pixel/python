f = open("numbers.txt", "r")
total = 0
max_num = None
min_num = None
for line in f:
    words = line.split()   
    for w in words:
        if w.isdigit():
            num = int(w)
            total = total + num
            if max_num is None or num > max_num:
                max_num = num                
            if min_num is None or num < min_num:
                min_num = num
print("Total:", total)
print("Maximum:", max_num)
print("Minimum:", min_num)
f.close()
