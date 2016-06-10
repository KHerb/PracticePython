user = int(raw_input("How many fibonacci numbers do you want return? "))
f = [1,1]
def fibonacci(f):
    return f.append(f[-2] + f[-1])

if user == 0:
    f.remove(f[0])
    f.remove(f[0])
    print f 
elif user ==1:
    f.remove(f[1])
    print f
elif user ==2:
    print f

for i in range(user-2):
    fibonacci(f)
    print f