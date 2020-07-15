def showMeAllList(mylist):
	count = 0 
	for i in mylist:
		print(i, " is the ", count,"index in the list")
		count+=1
	return mylist

##legoSets = ["skullarina","zombiecave","tiaga","pillager outpost","panda nersary "]
myluckNumbers = [1,2,3,4,5,6,7,8,9]
showMeAllList(myluckNumbers)