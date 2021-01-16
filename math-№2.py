min=10000000000
for x in range(-1000, 1001):
    x=x/1000
    for y in range(-1000, 1001):
        y=y/1000
        a=6*x**6 + 2*(x**4)*y**2 + 10*(x**2 + y**2) + 4 + 6*x*(y-1)
        if a<min:
            min=a
print(min)