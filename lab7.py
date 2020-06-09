from double_list import DoublyLinkedList
from lab6 import *

# Честно скажу, мало что понимаю, что именно от меня хочет 7 лаба !именно на пайтоне!
# Писать ооп на пайтоне это конечно совсем поехавший нужно быть :) 
# Просто с тем временем, что у меня осталось, сделать рабочие и хотя бы нормальные лабы на джаве уже не было возможности
# Скидывать сырой код я не хотел, по этому пишу на языке, который хотя бы понимаю

# На счёт 7 лабки спросил совета у Алексея Вадимовича
# Он сказал, что если я знаю что такое двусвязный список и могу его реализовать на питоне, а так же его методы,
# тогда вперёд. Я попытался что-то более-менее сделать, надеюсь хотя бы норм


train_1 = Train()
# print(train_1)
print("-"*10)
train_2 = Train()
# print(train_2)
print("-"*10)
train_3 = Train()
# print(train_3)
print("-"*10)
train_4 = Train()
train_5 = Train()
train_6 = Train()


doublelist_1 = DoublyLinkedList()
print(doublelist_1)
doublelist_1.traverse_list()

doublelist_2 = DoublyLinkedList()

doublelist_2.insert_in_emptylist(train_1)
doublelist_2.traverse_list()

doublelist_3 = DoublyLinkedList()
doublelist_3.insert_in_emptylist(train_6)
doublelist_3.insert_at_end(train_4)
doublelist_3.insert_at_end(train_3)
doublelist_3.reverse_linked_list()
doublelist_2.traverse_list()



# Методы:
# traverse_list(self) - отобразить
# insert_in_emptylist(self, data) - вставить в пустой
# insert_at_start(self, data)
# insert_at_end(self, data)
# insert_after_item(self, x, data)
# insert_before_item(self, x, data)
# delete_at_start(self)
# delete_at_end(self)
# delete_element_by_value(self, x)
# reverse_linked_list(self) 