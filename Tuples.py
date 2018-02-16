if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t= tuple(integer_list)
    print (hash(t))
    #튜플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는가 없는가이다. 
    # 즉, 리스트의 항목값은 변화 가능, 튜플의 항목값은 변화가 불가능
    # 따라서 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고싶지 않다면 주저하지 말고 튜플을 사용
    
    
    #   자바에도 hashcode가 있다.
    #   HashMap 같은 경우 동작 메카니즘은 key / value 쌍으로 자료를 처리하는 것이다.
    #   여기서 같은 내용의 key 객체인데 서로 다른 hash code를 가지고 있다면,
    #   다른 value를 가지는 데이터라는 오류가 발생
    #   [출처] [Java hash code] 해쉬 코드란?|작성자 맥서
