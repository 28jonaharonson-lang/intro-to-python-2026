grade = input("What is your grade?:")
if int(grade) >= 90:
    print ("Your grade is an A.")
if int(grade) >= 80 and int(grade) < 90:
    print ("Your grade is a B.")
if int(grade) >= 70 and int(grade) < 80:
    print ("Your grade is a C.")
if int(grade) >= 60 and int(grade) < 70:
    print ("Your grade is a D.")
if int(grade) < 60:
    print ("Your grade is an F. You fail.")