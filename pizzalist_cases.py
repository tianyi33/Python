pizza_topping="Please write all the topping you want to add: "
message=''
topping_list=[]
while pizza_topping!="quit":
	message=input(pizza_topping)
	pizza_topping.append(list(message))
	print(pizza_topping)
