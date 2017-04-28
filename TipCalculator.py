print "Welcome to Tip Calculator"
bill = float(input("What is the total bill amount? \n"))
group = int(input("And how many people were in your group? \n"))

if group>=8:
	rate = 0.2
else:
	rate = 0.15
tip = bill * rate
tip = round(tip,2)
total = bill+tip
total = round(total,2)
print "The tip amount on the bill is $", tip,  "bringing your total to $", total, "."