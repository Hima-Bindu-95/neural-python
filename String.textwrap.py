import textwrap
import math
def wrap(string, max_width):
    List=[]
    N=math.floor((len(string)/max_width))
    for i in  range(N):
      List.append((string[i*max_width:(i+1)*max_width]))
    R=((len(string)%max_width))
    List.append(string[N*max_width:(N+R)*max_width]) 
    return '\n'.join(List)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
