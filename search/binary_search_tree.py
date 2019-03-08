class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def breadth_first_for_each(self, cb):
    queue = []
    queue.append(self.value)
    print(queue)

    while len(queue) > 0:
      print(cb(queue[0]))
      queue.pop(0)

      if self.left is not None:
        queue.append(self.left)

      if self.right is not None:
        queue.append(self.right)

# py test_breadth_first_search.py

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value


arr = []    
cb = lambda x: arr.append(x)

b = BinarySearchTree(5)
b.insert(3)
b.insert(4)
b.insert(10)
b.insert(9)
b.insert(11)
print(b.breadth_first_for_each(cb))