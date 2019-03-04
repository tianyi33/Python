current_number=1
while current_number <=5:
	print(current_number)
	current_number+=1
# number<5
prompt= "\nTell me something, and I will repeat:"
prompt+="\nEnter 'quit' to end the program."
active=True
while active:
	message=input(prompt)
	if message == "quit":
		active = False
	else:
		print(message)