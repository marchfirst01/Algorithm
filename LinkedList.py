# Node 클래스 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# LinkedList 클래스 구현
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next # current.next(다음 노드)가 존재하지 않을 때 까지 next를 한다.
            current.next = Node(data)
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def insert(self, data, index):
        current = self.head
        for i in range(index-1):      # index-1번째 노드까지 이동
            current = current.next
        next_value = current.next       # index-1번째 노드의 next값 저장 
        current.next = Node(data)       # node 생성
        current = current.next
        current.next = next_value       # 새로 생성한 node의 next 값에 기존 node 연결
    def delete(self, index):
        current = self.head
        for i in range(index-1):
            current = current.next      # index-1번째 노드까지 이동
        target = current.next           # target에 index 노드 대입
        current.next = target.next      # current[index-1], target[index] -> current의 다음 node에 target의 다음 node[index+1]연결

Linked_List = LinkedList();
Linked_List.append('6');
Linked_List.append('AA');
Linked_List.append('11');
Linked_List.append('22');
Linked_List.append('33');
Linked_List.print_list();
print()
Linked_List.insert('1', 4);
Linked_List.print_list();
print()
Linked_List.delete(4);
Linked_List.print_list();
