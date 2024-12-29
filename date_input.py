date = input("Enter date in format mm-dd-yyyy: ")
month = date[0:2]
day = date[3:5]
year = date[-4:]
print(f"day = {day}, month = {month}, year = {year}")