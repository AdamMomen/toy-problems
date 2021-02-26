"""
1 -> A

1 + (64)
27 -> AA
how can 
number > 26?
	append a to the beginning the string and substract 26 

str = ""
number 28

28> 26? yes
str = "A"
number = 2
2 + 64

orb()
char()


"""
def number2string(number):
	if number > 0:
		return chr(number + 64)
	
def convertToColumnTitle(number):
	output = ""
	prefix = 0 

	while number > 26:
		prefix+=1	
		number = int(number/26)

	output += number2string(prefix)
	output += number2string(number)
	return output


print(convertToColumnTitle(28))
print(convertToColumnTitle(53))
print(convertToColumnTitle(703))
	
