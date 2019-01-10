def merge_the_tools(string, k):
    for i in range(1,(len(string)//k)+1):
        temp=[]
        for j in string[(i-1)*k:i*k]:
            if(j not in temp):
                temp.append(j)
                print(j,end="")
        print("")


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
