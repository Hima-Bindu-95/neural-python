# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=="__main__":
    import numpy
    n=numpy.array(list(map(int,input().split())))
    m=numpy.array(list(map(int,input().split())))
    print(numpy.inner(n,m))
    print(numpy.outer(n,m))
    
