from mosnter import User


p1 = input("Enter name:")
p2 = input("Enter name:")

u1 = User(p1)
u2 = User(p2)

u1.give_taco(u2)

print(u1)
print(u2)
