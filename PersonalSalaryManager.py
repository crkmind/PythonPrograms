# This code is created for personal purpose which calculates the amount for dailly expences and remaining salary.
#!/bin/python3
try:
	print("--------------------------------------------------------------------------------")
	print("Welcome to salary management program.")
	print("--------------------------------------------------------------------------------")
	
	
	sal = int(input("Please Enter Your This Month's Salary Default [6000] : ") or 6000)
	print("You have entered salary : ",sal)
	print("--------------------------------------------------------------------------------")
	
	
	month_exp=int(input("Please enter total amount for your monthly expences Default [1500] : ") or 1500)
	dailly=month_exp/30
	nd = int(dailly)
	sal -= month_exp
	print("You can spend : " +str(nd) ,"per day\nnow your total salary remaining is : " +str(sal))
	print("--------------------------------------------------------------------------------")
	
	
	clg=int(input("How much amount you want to save for college This moonth Default [3000] : ") or 3000)
	priv_amt=int(input("Please enter previous total collected college fees amount to add : "))

	print("Total collected amount for college is : ",clg + priv_amt )
	sal-=clg
	print("--------------------------------------------------------------------------------")
	
	
	anyother=input("Do you have any other deductions [Yes/No] Default [No] : ") or "No"
	if(anyother=="Yes"):
		ded=int(input("Enter total amount to deduct from salary : "))
		sal-=ded
		print("Total salary left after all deductions : ", sal)
	if(anyother=="No"):
		print("Total salary left after all deductions : ", sal)

	print("--------------------------------------------------------------------------------")
	print("Save it or Enjoy it :-)")
	print("--------------------------------------------------------------------------------")

except:
	print("Please Give The Correct Input")
