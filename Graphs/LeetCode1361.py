'''
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.
'''
#       Since every node can only have one parent,
        # in case we're inside a cycle the last node we visit
        # will have 2 parents
        
        
        
        # In the case we have an edge going in both directions
        # we can just check if the number of parents of the current node and their
        # childs is just equal to one
        
        # In the case when we have 2 or more connected components, when we see
        # A node that has no parent and it's different from 0 then we have found
        # a connected component
def find_root(n, lC, rC): # The root can be any of the n nodes
    aux_arr = [0]*n             # See test case 36
                                    # So first we have to find it
                                    # We are just looking the node that No
                                    # of parents == 0
    for i in range(n):
        l, r = lC[i], rC[i]
        if l != -1:
            aux_arr[l] += 1
        if r != -1:
            aux_arr[r] += 1
        
        root = -1
        for i in range(n):
            if aux_arr[i] == 0:
                root = i
                break
    return root
    
def validateBinaryTreeNodes(n, leftChild, rightChild):
    root = find_root(n, leftChild, rightChild)
        
    if root == -1:
        return False
        
    visited = [0]*n
    queue = [root]
    visited[root] = 1
        
    while queue:
        curr = queue.pop(0)
            
        l, r = leftChild[curr], rightChild[curr]
        if l != -1:
            if visited[l] == 1:
                return False
            visited[l] = 1
            queue.append(l)
        if r != -1:
            if visited[r] == 1:
                return False
            visited[r] = 1
            queue.append(r)
                
    for node in visited:
        if node == 0:
            return False
            
    return True
        
        