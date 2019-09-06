with open("output.txt") as fp:
	lines = fp.readlines()
	cnt = 0
	for line in lines:
		cnt += 1
	print cnt	

