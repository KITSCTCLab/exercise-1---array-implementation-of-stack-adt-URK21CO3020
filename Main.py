import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        
if lens(self.item)==0
    
    def is_full(self):
      
if len(self.items) >= size:
    def push(self, data):
        if not self.is_full():
            
if not self.is_full():
    def pop(self):
        if not self.is_empty():
            
if not self.is_empty():
    def status(self):
        
 for item in self.items:
# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
