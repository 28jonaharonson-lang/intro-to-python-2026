varA = input("What is your first number? (A):")
varB = input("What is your second number? (B):")

func = input("What type of mathematical function do you want to do?(Please type the full name of the function and capitalize the first letter) (I can do Multiplication, Division, Subtraction, Addition, Exponents, and Long Division):")
if func == ("Multiplication"):
    print(float(varA) * float(varB))
elif func == ("Division"):
    print(float(varA) / float(varB))
elif func == ("Addition"):
    print(float(varA) + float(varB))
elif func == ("Subtraction"):
    print(float(varA) - float(varB))
elif func == ("Exponents"):
    print(float(varA) ** float(varB))
elif func == ("Long Division"):
    print(divmod(float(varA), float(varB)))

else: print("Sorry, I don't understand that.")