# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    import numpy
    k = list(map(int,input().split()))
    a=[]
    b=[]
    for i in range(k[0]):
        a1=list(map(int,input().split()))
        a.append(a1)
    for i in range(k[0]):   
        b1=list(map(int,input().split()))
        b.append(b1)

    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print((numpy.floor_divide(a, b)))
    print(numpy.mod(a, b))
    print(numpy.power(a, b) )
    
