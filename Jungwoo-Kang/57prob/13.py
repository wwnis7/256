# What is the principal amount? 1500
# What is the rate? 4.3
# What is the number of years? 6
# What is the number of times the interest
# is compounded per year? 4
# $1500 invested at 4.3% for 6 years
# compounded 4 times per year is $1938.84.

principal=input("What is the principal amount? ")
rate=input("What is the rate? ")
years=input("What is the number of years? ")
com_years=input("What is the number of times the interest is compounded per year? ")
total=float(principal)*pow((1+float(rate)/float(com_years)),(float(com_years)*float(years))

print(f''' ${principal} invested at {rate}% for {years}
      compounded {com_years}times per year is {total}.''')

#뭐가 에러지;