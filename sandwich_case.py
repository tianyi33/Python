sandwich_orders=['beef','cheese','bacon','egg']
finished_sandwiches=[]
while sandwich_orders:
	finished_sandwich=sandwich_orders.pop()
	finished_sandwiches.append(finished_sandwich)
	print("I made a "+ finished_sandwich.lower()+" sandwich.")
for finished_sandwich in finished_sandwiches:
	print('All sandwiches are made '+finished_sandwich.lower())