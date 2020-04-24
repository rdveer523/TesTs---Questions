# CPP test-2
print("------------------------START---------------------------")
print("list obtained from list comprehension : ",[i+1 for i in range(5)])
print("variable length elements obtained from *args using list comprehension : \n",*[i+1 for i in range(5)])
print("---------------------------End\n\n")
d1 = {1:'a'}
d1[0] = 'b'
d1[1]='c'
print("Keys must be unique and takes updated Values :\n",d1)
print("---------------------------End\n\n")
d2 = {1:[2,3]}
print("NOTE: (1) LIST can not be treated as a KEY in dictionary because mutable and also unhashable.")
print("(2) TUPLE can consider as a KEY.")
d2[(2,3)]=1
#d2[[2,3]]=1
print(d2)
print("---------------------------End\n\n")
print("decima to binary : ",bin(10))
print("---------------------------End\n\n")
print("Decimal to Binary function")
def d2b(n1):
    if n1 > 1:
        k = []
        j=0
        while j<=1:
            print("quotient : ",n1//2)
            j = n1//2
            k.append(n1%2)
        print("Decimal to Binary : ", k)
    elif n1 <= 1:
        print("Please enter more than 1")
    else:
        print("Must be an integer")

    return k

if __name__ == "__main__":
    d2b(10)#int(input("Enter a number : ")))
print("---------------------------End\n\n")
print("-------------Using Recursion-------------------------")
def dec2bin(n2):
    if n2==0:
        return 0
    else:
        return (n2%2 + 10 * dec2bin(n2//2))

print(dec2bin(10))
print("---------------------------End\n\n")
print("---------------------------Recursive Function------------------------")

def fun(n3):
    a1=10
    a2=4
    if n3==1:
        return a1;
    else:
        return a2* fun(n3-1)

for i in range(1,6):
    print(fun(i))
print("---------------------------End\n\n")

a1 = '[1,2,3]'
a2 = '[4,5,6]'
print("List are in quotes so concatenated result is: ",a1+a2)
print("---------------------------End\n\n")

dd1 = {}
dd1[(1,2)]=3
dd1[3]=1,2
print("Dictionary keys collected as a list: ",list(dd1.keys()))
print("---------------------------End\n\n")

print(''.join('hello world'.split()))
print("---------------------------End\n\n")

print("Not return a list")
def fun1(arg): return arg.split()
print(fun1('hello'))

#def fun6(arg): return 'hello'.split()
#print(fun6('hello'))

def fun2(arg): return arg.split('hello')
print(fun2('hello'))

#def fun5(arg): return 'hello'.split(arg)
#print(fun5('hello'))

def fun3(arg): return list(arg)
print(fun3('hello'))

def fun4(arg): return arg.split('l')
print(fun4('hello'))
print("---------------------------End\n\n")


a=list(range(1,7))[:5]
b=[1,2,3,4,5,6][3:]
print(a+b)
print("---------------------------End\n\n")

print('helloWORLD'[2::2])
print("---------------------------End\n\n")


print("YIELD")
def yld(n1):
    for i in range(n1):
        yield i
    return None

if __name__ == '__main__':
    print(yld(3))
    print(tuple(yld(3)))
    print(list(yld(4)))
    
print("-----------------------------End\n\n")

print("Exceptional Hadling")
try:
    a=2+'2'
    print("Wrong")
except:
    print("Correct")

print("-----------------------------End\n\n")

print('2'*3)
print("-----------------------------End\n\n")
