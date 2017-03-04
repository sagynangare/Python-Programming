number1 = int(raw_input("Enter number of sweets:"))
number2 = int(raw_input("Enter number of bags:"))

whole_answer =number1 // number2
remainder_answer = number1 % number2

print("You will require ", whole_answer,"number of bags")
print("You will have reminder of :",remainder_answer,"sweets")
