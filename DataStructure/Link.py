class Node:
    def __init__(self, data, next= None):
        self.data = data
        self.next = next


def init():
    global node1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4


def delete(del_data):
    global node1
    pre_node = node1
    next_node = pre_node.next

    if pre_node.data == del_data:
        node1 = next_node
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break

        pre_node = next_node
        next_node = next_node.next


def insert(ins_data):
    global node1
    new_node = Node(ins_data)
    new_node.next = node1
    node1 = new_node


def print_list():
    global node1
    node = node1
    while node:
        print(node.data)
        node = node.next

    print()


def LinkedList():
    init()
    delete(2)
    insert("9")
    print_list()


LinkedList()


# 해시 테이블은 데이터를 저장할 때, 저장할 위치를 해시함수를 이용해서 생성합니다.
# 생성된 위치에 데이터를 저장하는 방식에서 사용하는 주소 테이블입니다.
# 순서 리스트와 연결 리스트 자료구조를 조합하여 사용하며, 데이터에 직접 접근이 가능하여 저장 및 읽기 속도가 빠름.
# 데이터 베이스에서 데이터를 저장할 때 주로 사용.