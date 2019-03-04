age=12
if age < 6:
	print('Please pay 10$.')
elif age< 12:
	print('Please pay 100$.')
elif age<20:
	print('Please pay 105$.')
else:
	print('Please pay 10000$.')
#age test 
alien_color=('black')
if alien_color is "green":
	print('you got 10 points')
elif alien_color is 'black':
	print("you got 1000000 points")
else:
	print('you got 100 points')
#alien color
usernames=['tianyi','aziz','bruce','jonah']
if usernames==[]:
	print('Anyone?')
for user in usernames:
	if user is 'tianyi':
		print("Greeting, Master "+ user.title()+'.\n')
	elif user is not 'tianyi':
		print("Please F off "+ user.title()+'.\n')
#name game
current_users=['a','b','coco','d','egg']
new_users=['Egg','f','g','u','COCO']
for current_user in current_users:
	if current_user.lower() in str(new_users).lower():
		print(current_user+' has been taken.')
	else:
		print("Thank you for join us.")
#new username










