import classes.Account as a

acc1 = a.Account('savings')
acc2 = a.Account('chequing', 1000)
print(acc1)
print(acc2)
print(repr(acc2))
acc1.add_transaction(10)
acc1.add_transaction(30)
acc1.add_transaction(50)
acc1.add_transaction(-20)
acc1.add_transaction(400)
acc1.add_transaction(-135)
acc1.add_transaction(2000)

