names = ['aziz', 'bruce', 'tianyi']
message1 = 'he is '+ names[2].title()+ '.'
message2 = names[0].title()+ ' has problems.'
print(message1+ ' '+message2)
# who is fucked up by python
fucked_up = names[0]
names.remove(fucked_up)
print( 'So '+fucked_up.title()+' was fucked up by python')
