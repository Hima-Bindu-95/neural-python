# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    In=input().strip()
    Out=input().strip()
    In_List=list(In)
    Out_List=list(Out)
    
    Final=[]
    for i in range(len(In_List)-len(Out_List)+1):
            Comp=[]
            Comp=(In_List[i:i+len(Out_List)])
            Final.append(Comp)
    
    Num=0
    Display_Final=[]
    for j in range(len(Final)):
        Display=[]
        if Out_List == Final[j]:
            Num=Num+1
            for i in range(len(Out_List)):
                Display.append(j+i)
            Display_Final.append(Display)
        
    
    
    
    for j in range(len(Display_Final)):
        print(f"({Display_Final[j][0]}, {Display_Final[j][-1]})")

    if Num==0:
        print(f"({-1}, {-1})")
