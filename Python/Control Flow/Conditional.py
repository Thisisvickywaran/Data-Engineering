
#Allow Access only if the user is logged in
#or they area is_guest
# but they must not be in banned


is_logged_in= True
is_guest= False
is_banned= True


print(is_logged_in or is_guest and  not is_banned) # without the brackets and is the first priority since its not our logic we cant use it 


print((is_logged_in or is_guest )and  not is_banned) # this is okay with out logic

