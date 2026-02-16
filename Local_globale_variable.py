x = 10

def outer():
    y = 5  
    def inner():
        nonlocal y
        global x
        z = 2  
        print("Local z:", z)
        print("Nonlocal y:", y)
        print("Global x:", x)
        y += 5
        x += 10

    inner()
    print("Nonlocal y after inner:", y)

outer()
print("Global x after function:", x)
