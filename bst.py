def main():
    class BSTNode:
        def __init__(self,data = None):
            self.data = data
            self.left = None
            self.right = None
# Add new data
        def insert(self,data):
            if not self.data:
                self.data = data
                return
            elif self.data == data:
                return
            elif data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BSTNode(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BSTNode(data)
# Find the minimum in the tree
        def get_min(self):
            current = self
            while current.left is not None:
                current = current.left
            return current.data 
# Find the maximum in the tree
        def get_max(self):
            current = self
            while current.right is not None:
                current = current.right
            return current.data
# Remove a piece of data
        def delete(self, data):
            if self.data == None:
                return None
            if data < self.data:
                if self.left is not None:
                    self.left = self.left.delete(data)
                return self
            if data > self.data:
                if self.right is not None:
                    self.right = self.right.delete(data)
                return self
            if self.data == data:
                if self.left is None:
                    return self.right
                if self.right is None:
                    return self.left
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.data = min_larger_node.data
            self.right = self.right.delete(min_larger_node.data)
# Find data in the tree
        def find(self, data):
            if self.data is None:
                return False
            if self.data == data:
                return True
            if data < self.data:
                return self.left.find(data)
            if data > self.data:
                return self.right.find(data)
# PostOrder the data
        def postorder(self, visited):
            if self.left is not None:
              self.left.postorder(visited)
            if self.right is not None:
              self.right.postorder(visited)
            if self.data is not None:
                visited.appened(self.data)
            return visited
# InOrder the data
        def inorder(self, visited):
            if self.left is not None:
                self.left.inorder(visited)
            if self.data is not None:
                visited.append(self.data)
            if self.right is not None:
                self.right.inorder(visited)
            return visited
#Find that data
        def exist(self, data):
            if self.data == data:
                return True
            if data < self.data:
                if self.left is None:
                    return False
                return self.left.exist(data)
            if data > self.data:
                if self.right is None:
                    return False
                return self.right.exist(data)

