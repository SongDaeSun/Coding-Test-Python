stack = [0, 1, 2]

print(stack)

stack.append(3)

print(stack)

stack.pop()

print(stack)




from collections import deque


queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)