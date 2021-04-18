resistencias = [100000, 100, 10000, 1000, 2200, 220, 22000, 4700, 470, 47000]

for r_d1 in resistencias:
	r_d2 = 9*r_d1
	print('R_d1 = {} Ohms, R_d2 = {} Ohms'.format(r_d1, r_d2))