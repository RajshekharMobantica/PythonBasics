import datetime

x = datetime.datetime.now()

#print datetime
print(x)

#print year and weekday
print(x.year)
print(x.strftime("%A"))


#create date object
y = datetime.datetime(2020, 5, 17)
print(y)

#Display name of month
z = datetime.datetime(2018, 6, 1)
print(z.strftime("%B"))


