if __name__ == '__main__':
    N = int(input())
    A=[]
    B=[]
    for i in range(N):
        A=(input().split())
        B.append(A)
    List=[]
    
    for i in range(N):
        if B[i][0]=='insert':
            List.insert(int(B[i][1]),int(B[i][2]))
        if B[i][0]=='print':
            print(List)
        if B[i][0]=='remove':
            List.remove(int(B[i][1]))
        if B[i][0]=='append':
            List.append(int(B[i][1]))
        if B[i][0]=='sort':
            List.sort()
        if B[i][0]=='pop':
            List.pop()
        if B[i][0]=='reverse':
            List.reverse()
       
        
            
