from  BinaryTree import BinaryTreeNode


def binary_search_tree_runner():
    
    binary_obj = BinaryTreeNode()
    try:
        nodes_count = int(input("Enetr how many nodes to insert into list:"))
    
    except Exception as e:
        print(e)
        print("enter number of nodes in integer only")
    nodes_list = []
    print('now enter all test cases')
    for i in range(0, nodes_count):
        nodes_list.append(int(input("enter:")))

    result = binary_obj.count_binary_search_tree(nodes_list)
    print("No of binary tree possiable in each test case is as follow")
    for i in result:
        print(i)

if __name__ == "__main__":
    binary_search_tree_runner()
