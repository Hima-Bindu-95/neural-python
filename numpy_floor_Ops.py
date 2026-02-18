# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    import numpy
    numpy.set_printoptions(legacy='1.13')
    
    my_array = numpy.array(list(map(lambda x:float(x),input().split())))
    print(numpy.floor(my_array))
    print(numpy.ceil(my_array))
    print(numpy.rint(my_array))
    
