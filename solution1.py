# Write code for algorithm 1 below
def count(num):
    if num == 0:
        print(num)
        return
    else:
        print(num) 
        (count(num-1))

n = 7
count(n)