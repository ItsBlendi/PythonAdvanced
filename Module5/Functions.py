def greet():
    print("Hello World!")

greet()

def greet_person(name):
    print("Hello,", name)

greet_person("aldin")
greet_person("Folrjon")

'''
def add(x,z):
    z=x+y
    return z
    
add(3,7)
'''


def add(x, y):
    z = x + y
    return z

result = add(3,7)

print("The result of 3+7 is =",result)