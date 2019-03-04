message='How old are you?'
message += '\nEnter ok when you finished.'
age=''
while age!='ok':
	age=input(message)
	if age!='ok':
		if age<3:
			print("Your kid is free for the ticket")
		elif age<12:
			print('10$ please.')
		elif age>12:
			print('15$ please.')
	
	
	
		