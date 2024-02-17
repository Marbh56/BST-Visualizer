from main import BSTNode

def test_bst_find():
    # Create a new BST
    bst = BSTNode()

    # Insert values
    values = [10, 5, 15, 2, 7]
    for value in values:
        bst.insert(value)

    # The inserted values should be found
    for value in values:
        assert bst.find(value) == True, f"Expected to find {value} in BST"

    # Values not inserted should not be found
    nonvalues = [1, 20, -1, 8]
    for value in nonvalues:
        assert bst.find(value) == False, f"Did not expect to find {value} in BST"
