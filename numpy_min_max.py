if __name__=='__main__':
    import numpy
    n=list(map(int,input().split()))
    my_array=[]
    for i in range(n[0]):
        A=list(map(int,input().split()))
        my_array.append(A)
    
    min_Axis_one= numpy.min(my_array, axis=1)
    max_of_minAone=numpy.max(min_Axis_one)
    print(max_of_minAone)
