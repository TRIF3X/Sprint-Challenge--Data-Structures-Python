Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
N/A , but typically it would be O(n) because we would be checking one by one

2. What is the space complexity of your `depth_first_for_each` function?
N/A, we would have to initialize a stack with an array. So worst case we could see O(n) depending on how big the tree is.

3. What is the runtime complexity of your `breadth_first_for_each` method?
O(n) in this case we won't find our item so we will have checked every item in the tree. This was more of a traversal of the entire tree.

4. What is the space complexity of your `breadth_first_for_each` method?
O(n), we will need to eventually handle all the nodes passed in within our queue copying them one at a time, if our tree is too big our array can overflow and we will have to initialize a new array with twice as much space. If we initialize an array with say 500 slots and only traverse a tree with less than 500 nodes we could stay at O(1) space complexity since we will never need more space and have are allocated the space we wanted.

5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
