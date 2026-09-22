def lists(n):
    _List = []
    for i in range(n):
        i = int(input())
        _List.append(i)

    print(f"numbers = {_List}")
    for i in range(1,(len(_List)-3)+1):
        if(i==3):
            continue
        print(_List[i])
   

n = int(input()) 
lists(n) 
