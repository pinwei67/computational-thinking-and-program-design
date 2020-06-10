weight = float(input("Enter Your Weight(KG)? "))
height = float(input("Enter Your height(M)? "))

bmi = weight / (height * height)

print("BMI指數為",bmi)

n = 0
left = 0
while n < 10:
    n = n + 1
    left = 10 - n
    print("這是第", n, "次的hello", "還有",left, "次機會")