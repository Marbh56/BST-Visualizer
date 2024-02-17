from bst import BSTNode, visualize_tree
      
gnome = BSTNode(10)
print(gnome.data)    # Output: 10
gnome.insert(56)
gnome.insert(2)
gnome.insert(5)
gnome.insert(75)
gnome.insert(65)
gnome.insert(19)
gnome.insert(564)
gnome.insert(60)
print(gnome.find(2))  # Output: True
print(gnome.find(30)) # Output: False
gnome.delete(2)
print(gnome.find(2))  # Output: False
print(gnome.get_min())  # Output: 10
print(gnome.get_max())  # Output: 56
visited_nodes = gnome.postorder([])
print(visited_nodes) # Output: [56, 10]
visited_nodes = gnome.inorder([]) 
print(visited_nodes) # Output: [10, 56]
visualize_tree(gnome)
