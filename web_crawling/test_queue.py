from Queue import LLQueue

q = LLQueue()

assert q.is_empty()

# Enqueue tests
q.enqueue(1)
print(str(q))
assert q.dequeue() == 1
assert q.is_empty()

q.enqueue(1)
assert not q.is_empty()
q.enqueue(2)
assert not q.is_empty()
q.enqueue(3)
assert not q.is_empty()
print(str(q))

assert q.dequeue() == 1
assert q.dequeue() == 2
assert q.dequeue() == 3
assert q.dequeue() == None
assert q.dequeue() == None
assert q.is_empty()