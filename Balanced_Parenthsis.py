from stack import Node
from stack import Stack

#creatig new stack
obj = Stack()
 
expression = input("enter any expression: ")

#function for balanced_parentheses
def balanced_parentheses(expression):
    open_parentheses = "({["
    closed_parethese = ")}]"
    
    for brackets in expression:
        if brackets in open_parentheses:
           bracts = Node(brackets)
           obj.push(brackets)
        elif brackets in closed_parentheses:
             obj.pop()

    if obj.is_empty():
       print("given expression is balanced")
    else:
        print("given expression is not balance")



balanced_parentheses(expression)
