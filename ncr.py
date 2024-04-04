def ncr(n,r):
	ans = 0
	temp_n = 1
	temp_r = 1

	for i in range(0,r):
		temp_n = temp_n * (n - i)
		if temp_n%(r-i) == 0:
			temp_n = temp_n/(r-i)
		else:
			temp_r = temp_r * (r - i)

	ans = temp_n/temp_r
	print(ans)
