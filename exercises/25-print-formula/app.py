C, H = 50, 30
D = 100,150,180
Q = list(map(lambda D: int(((2*C*D)/H)**(1/2)), D))
print(Q)