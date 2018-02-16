if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    set_t= set(arr)
    print("set_t",set_t)
    list_t = list(set_t)
    list_t.sort()
    print("list_t",list_t)
    print("len(list_t)",len(list_t))
 
   

    
