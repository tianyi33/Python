import random
random.random() 
number=random.randint(1,30)
guess="Guess what number it is?"
guess+="\nIf you want to know the answer just put 'please'."
message=""
active=True
while active:
	message=input(guess)
	if message<number:
		print("Guess bigger one, have some balls.")
	if message>number:
		print('Nonono too big dude.')
	if message==number:
		print('Guess what, your are right! The number is '+ str(number)+' .')
	if message=="please":
		active=False

