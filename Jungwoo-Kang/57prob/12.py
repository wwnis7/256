# Enter the principal: 1500
# Enter the rate of interest: 4.3
# Enter the number of years: 4
# After 4 years at 4.3%, the investment will
# be worth $1758.

principal=input("Enter the principal: ")
interest=input("Enter the rate of interest: ")
year=input("Enter the number of years: ")
# total=float(principal)*pow((1+0.01*float(interest)),float(year))
total=float(principal)*(1+0.01*float(interest)*float(year))
print(f'''After {year}years at {interest}%, the investment will
      be worth ${total}.'''  )