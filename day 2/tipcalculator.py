print("welcome to the tip calculator")
# bill=print(type(input("what was the total bill ? $"))) checking data type #str

bill=float(input("what was the total bill ? \n$ "))

tip=int(input("what percentage tip would you like to give ? 10 15 20 : \n"))

people=int(input("how many people do you want to split the bill between ?: \n"))

bill_with_tip= tip / 100 * bill +bill
print(bill_with_tip)

per_person=bill_with_tip/people

print(f"each person has to pay : ${per_person}")
