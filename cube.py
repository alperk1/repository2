number = int(input("Enter a Number:"))
for counter in range(number):
    if counter%3!=0 and counter%7!=0:
        print(counter)
    if counter % 3 == 0 and counter % 7 == 0:
            print("bipbop")
    if counter%3==0 and counter%7!=0:
        print("bip")
    if counter%7==0 and counter%3!=0:
        print("bop")
