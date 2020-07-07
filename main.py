
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
**************************

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
### create a function called myInformation()
## create and use these variables : myName,myAge,myCity
## but ake all of the variables to be taken by input.
### while designing the functiion we want to do the help documentation
def myInformation():

	"""
	Functionality:
	----------------
	(  ,   ) -> 

	Paramaters:
	-----------------
	1.
	2.

	Description:
	----------------
	This fucnction takes a .....

	"""
	myName = input("What is your name? : ") 
	myAge = float(input("What is your age? : "))
	myCity = input("What is your city? : ")
	

	if myAge <= 82:
		print(myName, "from",myCity,"can pcome to the party")
		return True
	else:
		print(myName, "from",myCity,"is not allowed to come to the party")
		return False

myInformation() ## test with age under 82
myInformation()	## test with age 82
myInformation() ## test with age over 82




