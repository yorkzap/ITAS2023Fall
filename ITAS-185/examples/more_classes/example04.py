import classes.MyClass as mc

my_object = mc.MyClass()
print(my_object.public_var)
print(my_object._protected_var)
print(my_object.__private_var)

x = my_object.get_private_var()
print(x)

my_object.set_private_var(21)
x = my_object.set_private_var()
print(x)
