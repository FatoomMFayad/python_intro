mark = int(input("Enter mark: "))
if 90<=mark<=100:
    print("Excellent")
elif 80<=mark<90:
    print("Very Good")
elif 70<=mark<80:
    print("Good")
elif 60<=mark<70:
    print("Fair")
elif 0<=mark<60:
    print("Fail")
else:
    print("Invalid mark")

