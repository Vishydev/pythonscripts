y = 5

def set_x(z):
    print ("Inner z:",z)
    x = z
    global y
    global a
    y = x
    a = 7

print("Y before setx = ", y)
set_x(10)
print("Y after setx = ", y)
# if 1<2:
#     x=5
print("A after setx = ", a)


print("Outer y = ", y)