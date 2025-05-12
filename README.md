#### mplement a program to detect a cycle in a linked list using data structures .


#### Run App :
``` python
python list.py
```

#### Use `hasCycle` Method To Detect Cycle and Returns `TRUE` or `FALSE` .
#### Implemetation
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

#### Thanks For Watching
#### © 2025, All rights reserved. Developed by Ho3ein Tahan