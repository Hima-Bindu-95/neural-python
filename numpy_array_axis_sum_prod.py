# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    import numpy
    n=list(map(int,input().split()))
    my_array=[]
    for i in range(n[0]):
        A=list(map(int,input().split()))
        my_array.append(A)


    Sum_Axis_zero=numpy.sum(my_array, axis = 0)

    Prod_of_Sum=numpy.prod(Sum_Axis_zero)
    print(Prod_of_Sum)  
