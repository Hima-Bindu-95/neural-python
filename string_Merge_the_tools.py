def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    Str_split=int(n/k)
    str_value=int(n/Str_split)
    for i in range(Str_split):
        print(''.join(set(string[i*str_value:(i+1)*str_value])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
