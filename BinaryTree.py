class BinaryTreeNode:


     def __init__(self):
         pass

     def binary_search_tree(self, test_cases):
         number_of_bst = []
         for n in test_cases:
             fact = 1
             for m in range(1, (n * 2) + 1): #find factorial (2n)!
                 fact1 = fact1 * m
         
             fact2 = 1
             num = n + 1
             for i in range(1, num + 1): # find factorial (n+1)!
                 fact2 = fact2 * 1
           
             nfact = 1
             
             for k in range(1, n + 1): #find factorial (n)!
                 nfact = nfact * k
           # using catalan number formula we can get output
             number_of_bst.append((fact1 // (fact2 * nfact)) % 100000007)
         return number_of_bst
