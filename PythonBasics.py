a=32
b=32.32
c=32+41j
print(a,b,c," ",type(a)," ",type(b)," ",type(c))
abc=int(input())
print(abc)
print(type(abc))

class test:
    def main():
        a=123
        b=321
        print(a+b)
test.main()


def main():
    a=float(input("Enter a decimal value => "))
    print(round(a,2))
main()



class Loops:
    def ForLoop():
        x=int(input("Enter a value => "))
        y=int(input("Enter second value => "))
        for i in range(x,y):
            print(i,end=" ")
Loops.ForLoop()
        
array_1=[1,2,3,4,5,5,"test1"]
array_2={1,2,3,4,5,5}
array_3=(1,2,3,4,5,5,"test")
array_4={
    "name":"test",
    "age":12,
    "gender":"male",
    "college":"NSEC",
    "salary":123456,
}
print(array_1,type(array_1))
array_1.insert("google")
array_1[1:4]=["test1","test2","test3","test5"]
print(array_1[-1])
print(array_1,type(array_1))
print(array_2,type(array_2))
print(array_3,type(array_3))
print(array_4,type(array_4))
