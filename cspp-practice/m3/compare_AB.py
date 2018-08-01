varA= input("")
varB= input("")

if (varA.isnumeric() and varB.isnumeric()):
	if (varA>varB):
		print("bigger")
	elif (varA==varB):
		print("equal")
	else:
		print("samller")
else:
	print("strings are involved")
