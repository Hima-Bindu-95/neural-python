# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=="__main__":
    import numpy
    n=list(map(int,input().split()))
    A=[]
    B=[]

    for i in range(n[0]):
        a=(list(map(int,input().split())))
        A.append(a)
    A=numpy.array(A)
    for i in range(n[0]):
        b=(list(map(int,input().split())))
        B.append(b)
    B=numpy.array(B)
    
    C = A @ B
    
    print(C)

    
