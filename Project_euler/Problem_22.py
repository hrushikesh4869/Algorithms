def get_value(name):
	value = 0
	for i in name:
		if i != '"':
			value = value + ord(i) - 64

	return value


with open("0022_names.txt") as file:
	data = file.read()
	data = data.split(',')
	data.sort()
	temp = 1
	ans = 0

	for i in data:
		ans = ans + get_value(i)*temp
		temp += 1

	print(ans)
