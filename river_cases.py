river={'chang jiang':'china',
	'huang he':'china',
	'qian tang jiang':'china',
	'nile':'egypt'}
for name,location in river.items():
	if location!="china":
		print(name.title()+" is not in my country.")
	else:
		print(name.title()+' is from my country!')

for name,location in river.items():
	print('\nthis river called '+ name.title()+' is located at '+location.title())

for name in river.keys():
	print(name.title())
