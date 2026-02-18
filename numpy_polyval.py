# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    import numpy
    coefficients=list(map(lambda x:float(x),input().split()))
    x_value=list(map(int,input().split()))
    result = numpy.polyval(coefficients, x_value)
    print(result[0])
