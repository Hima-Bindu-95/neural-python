import math
def average(array):
    # your code goes here
    Numerator=sum(set(array))
    denominator=len(set(array))
    Average=Numerator/denominator
    return Average
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
