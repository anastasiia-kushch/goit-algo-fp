class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self): 
        current = self.head 
        while current: 
            print(current.data) 
            current = current.next 

    def reverse(self):
        prev = None
        cur = self.head
        next_node = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head:
            return 

        sorted_head = None  
        current = self.head

        while current:
            next_node = current.next  
            
            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                cur = sorted_head
                while cur.next and cur.next.data < current.data:
                    cur = cur.next
                
                current.next = cur.next
                cur.next = current
            
            current = next_node  
        
        self.head = sorted_head  


    def merge_sorted(self, other):
        dummy = Node(0)
        current = dummy
        list1 = self.head
        list2 = other.head

        while list1 and list2:
            if list1.data < list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        self.head = dummy.next 





llist = LinkedList()
llist.insert_at_beginning(2)
llist.insert_at_beginning(4)
llist.insert_at_beginning(6)
llist.insert_at_end(8)
llist.insert_at_end(10)
# Реверсування списку
llist.reverse()
llist.print_list()
# Сортування вставками
llist.insertion_sort()
llist.print_list()


llist2 = LinkedList()
llist2.insert_at_beginning(1)
llist2.insert_at_beginning(3)
llist2.insert_at_beginning(5)
llist2.insert_at_end(7)
llist2.insert_at_end(9)
# Сортування вставками
llist2.insertion_sort()
llist2.print_list()

# Злиття відсортованих списків
llist.merge_sorted(llist2)
llist.print_list()




