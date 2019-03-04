users={"aziz":{'country':'turkey','city':'A','food':'rice'},
	"tianyi":{'country':'china','city':'B','food':'noodle'},
	"bruce":{'country':'us','city':'C','food':'burger'}}
for name, details in users.items():
	print('\nUsername: '+name)
	home=details['country']+' '+details['city']
	food=details['food']
	print('Came from '+home.title()+' .')
	print('He likes to eat '+food+' .')



