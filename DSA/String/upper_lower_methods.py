# islower() isupper() and isspace() methods in python

string = 'GeeksforGeeks is a computer Science portal for Geeks'
newstring = ''

for a in string:

	# Checking for lowercase letter and
	# converting to uppercase.
	if a.isupper() == True:

		newstring += a.lower()

	# Checking for uppercase letter and
	# converting to lowercase.
	elif a.islower() == True:

		newstring += a.upper()


print("In original String : ")
print(newstring)
