# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=="__main__":
    import numpy
    n=list(map(int,input().split()))
    A=[]
    for i in range(n[0]):
        a=(list(map(lambda x:float(x),input().split())))
        A.append(a)
    A=numpy.array(A)
    print(round(numpy.linalg.det(A),2))
    
