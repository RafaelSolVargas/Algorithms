"""
A Tree is hierarchical structure where data is organized hierarchically and are linked together, the difference to linked list is that items are not linked in linear order. 
Binary Search Trees are Trees where the Nodes are ordered by some logic. 



General Tree:
A general tree is a tree data structure where there are no constraints on the hierarchical structure. 
-> Follow properties of a tree
-> A Node can have any number of children
-> Used for folder hierarchy

Binary Tree:
In the Binary Tree we have:
-> Follow the properties of a tree
-> A Node can have at most two child nodes, left and right

Binary Search Tree:
Specialization of Binary Tree, in this case the value stored in the left child of any node should be lesser than the value in the parent node and this one should be lesser than the right child value
left < parente < right 
It's used for simple sorting algorithms, priority queues and applications where data are constantly entering and leaving

AVL Tree:
It's a self balancing binary search tree. This is the first tree introduced which automatically balance its height. 
-> Specialization of binary search trees
-> Self Balancing
-> Each node store a value called a balance factor which is the difference in height between its left and right subtrees.
-> All nodes must have a balance factor of -1, 0 or 1.
Most used in situations where frequent insertions are involved
Used in Memory management subsystem of the the Linux kernel to search memory regions of process during preemption.

Red-Black Tree:
Another specialized tree that deals with self-balancing.
-> Each node is either red or black
-> Every path from a given node to any of its leaf nodes must go through the same number of black nodes
Used as a base for data structure used in computational geometry
Used in the Completely Fair Scheduler used in current Linux Kernels
Used in the epoll system call implementation of Linux Kernel

Splay Tree:
The main difference in this type of tree is that after performing search, insertion or deletion, the tree perform an action called splaying, where the tree is rearranged (using rotations) so that the particular element is placed at the root of the tree
Used to implement caches
Used in garbage collectors
Used in data compression
"""


# All this information was collected in this article: https://towardsdatascience.com/8-useful-tree-data-structures-worth-knowing-8532c7231e8c
