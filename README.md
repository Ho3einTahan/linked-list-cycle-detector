#### Implement a Program to Detect a Cycle in a Linked List Using Data Structures


#### Run App :
``` python
python list.py
```
#### Usage :
#### Use `hasCycle` Method To Detect Cycle and Returns `TRUE` or `FALSE` .

#### Implementation :
``` python
lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)

first = lst.head
second = first.next
third = second.next
fourth = third.next

fourth.next = second

lst.hasCycle()
```

#### Thanks for Watching!

#### © 2025, All rights reserved. Developed by Ho3ein Tahan