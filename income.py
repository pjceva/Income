# Get value 
value = float(input("Please insert the amount to invest: "))

#Getting Income rate
rate = int(input("Please insert the % income rate: "))/100 + 1

#Getting year
year = int(input("Please insert in how many years you wish to know your new income: "))

#calculating income
income = value * rate
for i in range(1, year):
    income = income * rate

print (income)
