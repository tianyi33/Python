def make_sandwich(name,*addings):
	print('Dear '+name+',')
	for adding in addings:
		print('You want to put '+ adding)
make_sandwich('tianyi',"beef","vege",'ranch')

