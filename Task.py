a = 1

while a <= 50:
    if a % 3 == 0 and a % 5 == 0:
        print("Dangdut")
        a += 1
    elif a % 3 == 0 :
        print("Dang")
        a += 1
    elif a % 5 == 0 :
        print("Dut")
        a += 1
    else:
        print(a)
        a += 1