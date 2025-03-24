height = int(input("Enter height: "))

for i in range(1, height+1):
    if i % 2 != 0:
        odd_factor = int((i-1)/2)
        print("AA" + odd_factor*"BBAA")
    else:
        even_factor = int((i - 2) / 2)
        print("BBAA" + even_factor*"BBAA")