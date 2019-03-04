dinner_list=['tianyi','bruce','aziz','liudy','javid']
invitation='Please join us for dinner '
print(invitation+str(dinner_list))
cannot= dinner_list.pop(3)
print(cannot+" connot come")
dinner_list.insert(3,"liudy replacement")
print(invitation+str(dinner_list)) 
print('Sorry, dinner is only for 2 people.')
sorry_guys1=dinner_list.pop(0)
print('sorry, '+str(sorry_guys1.title())+' you are not invited.')
sorry_guys2=dinner_list.pop(0)
print('sorry, '+str(sorry_guys2.title())+' you are not invited.')
sorry_guys3=dinner_list.pop(0)
print('sorry, '+str(sorry_guys3.title())+' you are not invited.')
print('Hey! '+str(dinner_list[0].title())+' ,dude, you are in!')
print('Hey! '+str(dinner_list[1].title())+' ,dude, you are in!')
number=len(dinner_list)
print(number)
del dinner_list[0]
del dinner_list[0]
print(dinner_list)



