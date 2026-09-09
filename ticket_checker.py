age = int(input("How old are you? "))

is_adult = age >= 18

print("Is adult:", is_adult)

if is_adult:
    print("Adult ticket price: KSh 1,000")
else:
    print("Child ticket price: KSh 500")
