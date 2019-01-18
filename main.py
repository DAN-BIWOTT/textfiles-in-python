import string
from typing import List

fileName: str = input("Enter the file name: ")

fo = open(fileName, "r")
number = 0
items: List[str] = fo.readlines()
money = 0
for y in items:
    name = items[number]
    mine = name.replace("Â", '')
    Myname: List[str] = mine.split(",")
    first_name = Myname[0] #first name
    other_names = Myname[1]
    lastNameL: List[str] = other_names.split("date=")
    lastNames = lastNameL[0] #other names
    dates = lastNameL[1]
    cashL = dates.split("$")
    cash = cashL[1] #cash
    tarehe = cashL[0] #dates
    edit_date = tarehe.split("/")
    day = edit_date[0]
    month = edit_date[1]
    year = edit_date[2]
    final_year = (int(year)%100)
    cash = cash.strip()
    temp = len(cash)
    if temp < 5:
        cash = " "+ cash
    if temp < 6:
        cash = " "+ cash
    print(day + "/" + month + "/" + str(final_year) + " " + lastNames + " " + first_name + " $" + cash)
    number = number + 1
    money = float(cash) + money

print("\n")
print("Total: $"+ str(money))
fo.close()
