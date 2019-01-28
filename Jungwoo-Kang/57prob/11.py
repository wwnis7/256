# How many euros are you exchanging? 81
# What is the exchange rate? 137.51
# 81 euros at an exchange rate of 137.51 is
# 111.38 U.S. dollars.

money=input("How many euros are you exchanging? ")
ex_rate_from=input("What is the exchange rate? ")
ex_rate_to=input("What is the exchange rate to? ")
US=float(money)*float(ex_rate_from)/float(ex_rate_to)
print(f"""{money} euros at an exchange rate of {ex_rate_from} is
      {round(US,2)}.""")