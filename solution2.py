# Write code for algorithm 2 below
def natural_numbers(x,i=1):
	if x > i:
		return 
	else:
		print(i)
		natural_numbers(x,i+1)
natural_numbers(3)
#output: 1 2 3