import string
def print_rangoli(size):
    # your code goes here
    #5 +(5-1)+(2*n-2)
    L=[]
    L_rangoli=4*size-3
    L=(string.ascii_lowercase[:size][::-1])
    
    if size>=2:
        #top
        for i in range(size-1):
            print((''.rjust(2*size-2-2*i,'-')+'-'.join(L[0:i+1])+'-'+'-'.join(L[0:i][::-1])).ljust(L_rangoli,'-'))
        
        #center
        print('-'.join(L)+'-'+'-'.join(L[0:size-1][::-1]))
        #bottom
        for i in range(size-1,0,-1):
            print((''.rjust(2*size-2*i,'-')+'-'.join(L[0:i])+'-'+'-'.join(L[0:i-1][::-1])).ljust(L_rangoli,'-'))
    elif size==1:
        print(L[0])
    else:    
        print()
    


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
