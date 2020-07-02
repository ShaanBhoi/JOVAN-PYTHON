
'''****************************
** 	HOW TO CREATE A VARIABLE 
**	variable_name = value 
**
**	HOW TO CALL A FUNCTION 
** 	function_name(param1,param2,...,param#)
**
**	BACKWARD SLASH FUN \
**	\t makes a new tab 
**	\n makes a new line 
**************************'''

############################ last class functions below	
def division(num1,num2):
	'''
	Functionality:
	----------------
	(int,int) -> bool

	Paramaters:
	-----------------
	1. num1 and this stores the first value of an integer to be divided
	2. num2 and this stores the second value of an integer to be divided

	Description:
	----------------
	This fucnction takes two integers, num1 & num2 ,and divides them and outputs the two possibilities , always returns True

	Example:
	----------------
	> division(3,4)
	3 /	4  =  0.75
	4 / 3  =  1.3333333333333333
	True 

	
	> division(num1,num2)
	3 / 4  =  0.75
	4 / 3  =  1.3333333333333333
	True

	
'''
	res1 = num1 / num2 
	res2 = num2 / num1

	print(num1,"/",num2," = ",res1)
	print(num2,"/",num1," = ",res2)
	
	return True

def modulo(num1,num2):
	'''
	Functionality:
	----------------
	(int,int) -> bool 

	Paramaters:
	-----------------
	1. num1 and this stores the first value of an integer to be modded
	2. num2 and this stores the second value of an integer to be modded

	Description:
	----------------
	This fucnction takes two integers, num1 & num2 , and mods them and outputs the two possibilities, always returns True

	Example:
	----------------
	> modulo(3,4)
	3 %	4  =  3
	4 % 3  =  1
	True 

	> num1 = 3
	> num2 = 4
	> modulo(num1,num2)
	3 % 4  =  3
	4 % 3  =  1
	True

'''
	res1 = num1 % num2 
	res2 = num2 % num1

	print(num1,"%",num2," = ",res1)
	print(num2,"%",num1," = ",res2)
	
	return True	

def addition(num1, num2):
	'''
	Functionality:
	----------------
	(int,int) -> int

	Paramaters:
	-----------------
	1. num1 and this stoers the first value of an integer to be added
	2. num1 and this stoers the first value of an integer to be added

	Description:
	----------------
	This fucnction takes two integers, num1 & num2 , and adds them and outputs the result. Returns int of result.

	Example:
	----------------
	> addition(4,3)
	4 + 3 = 7
	7

	> num1 = 4
	> num2 = 3
	>addition(num1,num2)
	4 + 3 = 7
	7
'''
	sum = num1 + num2
	print(num1,"+",num2," = ",sum)
	return sum

def subtraction(num1, num2):
	'''
	Functionality:
	----------------
	(int,int) -> bool

	Paramaters:
	-----------------
	1. num1 and this stores the first value of an integer to be subtracted
	2. num2 and this stores the second value of an integer to be subtracted

	Description:
	----------------
	This fucnction takes two integers, num1 & num2 ,and subtracts them and outputs the two possibilities , always returns True

	Example:
	----------------
	> subtraction(3,4)
	3 - 4 = -1
	4 - 3 = 1
	True

	> num1 = 3
	> num2 = 4
	>subtraction(num1,num2)


	3 - 4 = -1
	4 - 3 = 1
	True

'''
	res1 = num1 - num2 
	res2 = num2 - num1

	print(num1,"-",num2," = ",res1)
	print(num2,"-",num1," = ",res2)

	return True

def multiplicationGenerator(num1,num2):
	'''
	Functionality:
	----------------
	(  ,   ) -> 

	Paramaters:
	-----------------
	1.
	2.
	3.

	Description:
	----------------
	This fucnction takes a .....

	Example:
	----------------
	> 

'''
	product = num1*num2
	print(num1,"x",num2," = ",product)

def singleTable(num1,num2):
	'''
	Functionality:
	----------------
	(  ,   ) -> 

	Paramaters:
	-----------------
	1.
	2.
	3.

	Description:
	----------------
	This fucnction takes a .....

	Example:
	----------------
	> 

'''
	count = 0
	while count<=num2:
		multiplicationGenerator(num1,count)
		count+=1

def main_calculator():
	print("WELCOME TO JOVANS CALCULATOR")
	num1 = int(input("What is your first number? : "))
	num2 = int(input("what is your second number? : "))	
	user_input = int(input("Press 1 for divison\nPress 2 for addition\nPress 3 for subtraction\nPress 4 for the multiplication\nPress 5 for a single multiplicaiton table\nPress 6 for modulo\n\tEnter input here: "))
### if the user input is exactly equal to 1, then we want to call the division function. 
### make a call to the function with the name division(num1,num2), inside of the true if statement
### have an ekse statenent 

	if user_input == 1:                                                         
		division(num1,num2)
	elif user_input == 2:
		addition(num1,num2)

	elif user_input == 3:
		subtraction(num1,num2)

	elif user_input == 4:
		multiplicationGenerator(num1,num2)


	elif user_input == 5:
		singleTable(num1,num2)	

	elif user_input == 6:
		modulo(num1,num2)		
	else:
		print("ERROR!!! please try again")
		main_calculator()

	return True


###main_calculator()


'''
	Functionality:
	----------------
	(  ,   ) -> 

	Paramaters:
	-----------------
	1.
	2.
	3.

	Description:
	----------------
	This fucnction takes a .....

	Example:
	----------------
	> 

'''
	