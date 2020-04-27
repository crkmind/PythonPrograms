# This code is created for personal purpose which calculates the amount for dailly expences and remaining salary.

print("Welcome to salary management program.")


sal = int(input("Please Enter Your This Month's Salary : "))
print("You have entered salary : ",sal)


month_exp=int(input("Please enter total amount for your monthly expences : "))
dailly=month_exp/30
nd = int(dailly)
sal -= month_exp
print("You can spend : " +str(nd) ,"per day\nnow your total salary remaining is : " +str(sal))


clg=int(input("How much amount you want to save for college This moonth : "))
priv_amt=int(input("Please enter your total collected college fees amount : "))


print("Total collected amount for college is : ",clg + priv_amt )


sal-=clg


anyother=input("Do you have any other deductions [Yes/No] Default [No] : ") or "No"

if(anyother=="Yes" or "yes" or "y" or "Y"):
	ded=int(input("Enter total amount to dedeuct from salary : "))
	sal-=ded
	print("Total salary left after all deductions : ", sal)
  
if(anyother=="No" or "no" or "n" or "n"):
	print("Total salary left after all deductions : ", sal)

else:
	print("Please Enter Correct Value Yes/No/Y/N/yes/no/y/n")


print("Save it or Enjoy it :-)")

