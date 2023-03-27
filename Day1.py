# CODE:
a = []
for i in range(5):
    inp = int(input("{0}]Enter number: ".format(i+1)))
    a.append(inp)
    i+=1

a.sort()
# Smallest number in inputs:
print("\nSmallest number: ",a[0])
# Largest number in inputs:
print("\nLargest number:", a[4])

# INPUTS:
1] Enter number: 5
2] Enter number: 6
3] Enter number: 14
4] Enter number: 25
5] Enter number: 9
	
# OUTPUT:
Smallest number: 5	

Largest number: 25
