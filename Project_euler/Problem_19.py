def get_days(month, year):

	if month == 2 :
		if year % 100 == 0 and year % 400 != 0:
			return 28
		if year % 4 == 0:
			return 29
		else:
			return 28

	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		return 31
	else:
		return 30

ans = 0
count  = -1
var = 1

for year in range(1901, 2001):
	for month in range(1, 13):
		for day in range(1, get_days(month, year)+1):
			var += 1
			if var > 7:
				var  = 1
			if var == 7 and day == 1:
				ans += 1

print(ans)
