def find_total(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Total:", total)

find_total(10, 20)
find_total(5, 15, 25, 35)
find_total(1, 2, 3, 4, 5)
