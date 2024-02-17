def main():
    class BSTNode:
        def __init__(self,data = None):
            self.data = data
            self.left = None
            self.right = None

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

        def get_min(self):
            current = self
            while current.left is not None:
                current = current.left
            return current.data 
        
        def get_max(self):
            current = self
            while current.right is not None:
                current = current.right
            return current.data
        
        def delete(self, data):
            # Case That Deals with a leaf aka No Children Nodes
            if self.left == data:
                