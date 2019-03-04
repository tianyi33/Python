import random
random.random() 
number=random.randint(1,40)
guess="Guess what number it is(between 1 to 40)?"
guess+="\nIf you want to know the answer just put 'please'."
message=""
while message !='please':
	message=input(guess)
	if message=='please':
		break
	if message<number:
		print("Guess bigger one, have some balls.")
	if message>40:
		print("Are you stupid?? What words you cannot understand? 4 or 0??")
	if 40>message>number:
		print('No No No too big dude.')
	if message==number:
		print('Guess what, you are right! The number is '+ str(number)+' .')
		break



