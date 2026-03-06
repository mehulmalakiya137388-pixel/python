f = open("marks.txt", "r")
for line in f:
    data = line.strip().split(",")
    roll = data[0]
    name = data[1]
    m1 = int(data[2])
    m2 = int(data[3])
    m3 = int(data[4])
    m4 = int(data[5])    
    total = m1 + m2 + m3 + m4
    per = total / 4
    if per >= 75:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 50:
        grade = "C"
    else:
        grade = "D"
    print("Roll No:", roll)
    print("Name:", name)
    print("Total:", total)
    print("Percentage:", per)
    print("Grade:", grade)
    print()
f.close()
