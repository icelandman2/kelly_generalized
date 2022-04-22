
def calc_price(n, k=6., verb=False):
	if n <= 0:
		return 0
	elif n == 1:
		return (1.+k)/2
	else:
		ret = [0]*(n+1)
		ret[1] = (1.+k)/2.
		for i in range(2, n+1):
			prev_val = ret[i-1]
			max_pay = int(prev_val)
			prev_chance = prev_val * (1-((k-max_pay)/k))
			new_chance = (max_pay+k+1)/(2.) *  ((k-max_pay)/k)
			ret[i] = prev_chance+new_chance
		if verb:
			print(ret)
		return ret[n]

def kelly(observed_price, fair_price, k=6.):
	p = fair_price/k
	p_o = observed_price/k
	b = (k-observed_price)/observed_price
	return round(p + (p-1)/b, 5)

k=6
rolls = 2
v = calc_price(rolls, k=k, verb=False)
kel = kelly(4.25, v, k=k)
print(kel)



'''
criterion

f = p - q/b = p + (p-1)/b

f = fraction to wager
p = p(win)
q = p(lose)
b = proportion gained with win
'''