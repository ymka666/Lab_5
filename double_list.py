class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        """Вставляет элемент в пустой сисок"""
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("List is not empty.")

    def insert_at_start(self, data):
        """Вставляет в начало списка"""
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("Node inserted.")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        """Вставляет в конец списка"""
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        """Вставляет после конкретного элемента"""
        if self.start_node is None:
            print("List is empty.")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("Item not in the list.")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        """Вставляет перед конкретным элементом"""
        if self.start_node is None:
            print("List is empty.")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("Item not in the list.")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def traverse_list(self):
        """Выводит список"""
        if self.start_node is None:
            print("List has no elements.")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def delete_at_start(self):
        """Удалить в начале"""
        if self.start_node is None:
            print("The list has no element to delete.")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def delete_at_end(self):
        """Удалить в конце"""
        if self.start_node is None:
            print("The list has no element to delete.")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def delete_element_by_value(self, x):
        """Удалить элемент по значению"""
        if self.start_node is None:
            print("The list has no element to delete.")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found.")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found.")

    def reverse_linked_list(self):
        """Перевернуть список"""
        if self.start_node is None:
            print("The list has no element to reverse.")
            return
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p



#Для проверки

# new_linked_list = DoublyLinkedList()
# new_linked_list.traverse_list()
# new_linked_list.insert_in_emptylist(50)
# new_linked_list.traverse_list()
# print("-"*10)
# new_linked_list.insert_at_start(10)
# new_linked_list.insert_at_start(5)
# new_linked_list.insert_at_start(18)
# new_linked_list.traverse_list()
# print("-"*10)
# new_linked_list.insert_at_end(29)
# new_linked_list.insert_at_end(39)
# new_linked_list.insert_at_end(49)
# new_linked_list.traverse_list()
# print("-"*10)
# new_linked_list.insert_after_item(50, 65)
# new_linked_list.traverse_list()
# print("-"*10)
# new_linked_list.insert_before_item(29, 100)
# new_linked_list.traverse_list()
# print("-"*10)
# new_linked_list.delete_at_start()
# new_linked_list.traverse_list()
# print("-"*10)
# new_linked_list.delete_at_end()
# new_linked_list.traverse_list()
# print("-"*10)
# new_linked_list.delete_element_by_value(65)
# new_linked_list.traverse_list()
# print("-"*10)
# new_linked_list.reverse_linked_list()
# new_linked_list.traverse_list()