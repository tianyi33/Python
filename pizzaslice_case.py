pizzas=['apple','cheese','hotdog','holyshit']
for pizza in pizzas:
	print(pizza)
copy_pizzas=pizzas[:]
print(copy_pizzas)
pizzas.append('monster\n')
print('My choices of pizza are:')
for pizza in pizzas:
	print(pizza)
copy_pizzas.append('pinapple')
print("Aziz's chices of pizza are:")
for copy_pizza in copy_pizzas:
	print(copy_pizza)
