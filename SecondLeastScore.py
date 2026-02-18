if __name__ == '__main__':
    output = []
    scoreL = []
    SecondLowest_List = []
    for _ in range(int(input())):
        input_list = []
        name = input()
        score = float(input())
        input_list.append(name)
        input_list.append(score)
        output.append(input_list)
        scoreL.append(score)
        output=sorted(output)
        sorted_list = sorted(output, key=lambda x: x[1])
        ScoreL_list = sorted(scoreL)
   
    Unique_list=list(set(ScoreL_list))
    SecondLowest=Unique_list[1]
    
    for j in range(len(ScoreL_list)):
        if SecondLowest ==ScoreL_list[j]:
            SecondLowest_List.append(sorted_list[j][0])
    print("\n".join(sorted(SecondLowest_List)))
