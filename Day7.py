# CODE

def prime(num):
	if num<2:
		return False
	for i in range(2, int(num**0.5) + 1):
		if num%i == 0:
			return False
	return True

num = int(input("Enter a number: "))
if prime(num):
	print("{} is prime number".format(num))
else:
	print("{} is not prime".format(num))
	
# INPUT OUTPUT


#Enter a number: 105
#105 is not prime
