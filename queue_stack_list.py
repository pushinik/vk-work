##############################
print("1. Циклический список")
##############################

def hasCycle(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

node1 = Node(11)
node2 = Node(3)
node3 = Node(8)
node4 = Node(9)
node5 = Node(6)
node6 = Node(11)
node7 = Node(16)
node8 = Node(17)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

print(hasCycle(node1))

node8.next = node3

print(hasCycle(node1))

#########################################
print("2. Развернуть односвязный список")
#########################################

def reverseLinkedList(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def print_node(node):
    values = []
    while node:
        values.append(str(node))
        node = node.next
    print(" ".join(values))

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

print_node(node1)
print_node(reverseLinkedList(node1))

#################################
print("3. Найти середину списка")
#################################

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

node1 = Node(3)
node2 = Node(8)
node3 = Node(9)
node4 = Node(6)
node5 = Node(11)
node6 = Node(16)
node7 = Node(17)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

print_node(node1)
print(middleNode(node1))

################################################
print("4. Удаление элемента из связного списка")
################################################

def removeElements(head, val):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    cur = head
    while cur is not None:
        if cur.value == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

print_node(node1)

removeElements(node1, 3)
print_node(node1)

###############################################################
print("5. Является ли одна строка исходной для другой строки?")
###############################################################

from collections import deque

def isSubsequence(a, b):
    q = deque(a)
    for el in b:
        if q and q[0] == el:
            q.popleft()
    return len(q) == 0

print(isSubsequence(["a", "b", "d"], ["u", "a", "b", "q", "d"]))
print(isSubsequence(["a", "u", "d"], ["u", "a", "b", "q", "d"]))

def isSubsequence(a, b):
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)

print(isSubsequence(["a", "b", "d"], ["u", "a", "b", "q", "d"]))
print(isSubsequence(["a", "u", "d"], ["u", "a", "b", "q", "d"]))

def isSubsequence(a, b): # не учитывает порядок
    i = 0
    lenA = len(a)
    lenB = len(b)
    for el1 in range(lenA):
        for el2 in range(lenB):
            if a[el1] == b[el2]:
                i += 1
                break
    return i == lenA

print(isSubsequence(["a", "b", "d"], ["u", "a", "b", "q", "d"]))
print(isSubsequence(["a", "u", "d"], ["u", "a", "b", "q", "d"]))

##########################################
print("6. Является ли слово палиндромом?")
##########################################

def isPalindrome(s):
    stack = deque(s)
    for char in s:
        if char != stack.pop():
            return False
    return True

print(isPalindrome("abcba"))
print(isPalindrome("abab"))
print(isPalindrome("ababa"))

def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome("abcba"))
print(isPalindrome("abab"))
print(isPalindrome("ababa"))

################################################
print("7. Слияние двух отсортированных списков")
################################################

def mergeSortedLists(a, b):
    dummy = Node(0)
    cur = dummy
    while a and b:
        if a.value <= b.value:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next
        cur = cur.next
    cur.next = a if a else b
    return dummy.next

node1 = Node(3)
node2 = Node(6)
node3 = Node(8)

node4 = Node(4)
node5 = Node(7)
node6 = Node(9)
node7 = Node(11)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6
node6.next = node7

print_node(node1)
print_node(node4)
mergeSortedLists(node1, node4)
print_node(node1)
