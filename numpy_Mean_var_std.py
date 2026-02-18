# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    import numpy
    numpy.set_printoptions()
    n=list(map(int,input().split()))
    my_array=[]
    
    for i in range(n[0]):
        A=list(map(int,input().split()))
        my_array.append(A)

    Mean_List=numpy.mean(my_array,axis=1)
    Var_list=numpy.var(my_array,axis=0)
    Std_list=numpy.std(my_array,axis = None)
  
    print(Mean_List)
    print(Var_list)
    
    if Std_list == 0:
            print("0.0")
    else:
            print(f"{Std_list:.11f}")
