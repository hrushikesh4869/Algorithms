my_dict = {
	1 : 3,
	2 : 3,
	3 : 5,
	4 : 4,
	5 : 4,
	6 : 3,
	7 : 5,
	8 : 5,
	9 : 4,
	10 : 3, 
	11 : 6,
	12 : 6,
	13 : 8,
	14 : 8,
	15 : 7,
	16 : 7,
	17 : 9,
	18 : 8,
	19 : 8,
	20 : 6,
	30 : 6,
	40 : 5,
	50 : 5,
	60 : 5,
	70 : 7,
	80 : 6,
	90 : 6
}

hundred = 7
thousand = 8
And = 3


def num_to_char(num):
	
	if num > 0 and num <= 20:
		return my_dict[num]

	if num < 100 and num % 10 == 0:
		return my_dict[num]

	if num % 100 == 0 and num < 1000:
		return my_dict[num//100] + hundred

	if num == 1000:
		return thousand + 3

	if num < 100:
		tens = (num//10)*10
		ones = num % 10
		return my_dict[tens] + my_dict[ones]

	if num > 100 and num < 1000:
		hundreads = num//100
		tens = ((num // 10)%10) * 10
		ones = (num % 10)
		last_two = tens + ones
		if my_dict.get(last_two) != None:
			return my_dict[hundreads] + hundred + And + my_dict[last_two]

		return my_dict[hundreads] + hundred + And + my_dict[tens] + my_dict[ones]



ans = 0

for i in range(1, 1001):
	ans = ans + num_to_char(i)

print(ans)
