class Stack(object):
      def __init__(self):
          self.values = []
      
      def push(self,value):
        #add top of the stack
          self.values.append(value)
     
      def pop(self):
          #remove values
          return self.values.pop()

class Queue(object):
      def __init__(self):
          self.values = []
  
      def push(self,value):
          self.values.append(value)
     
      def pop(self):
          return self.values.pop(0)
        


stack = Stack()

queue = Queue()


class Palindrome_checker(object):
#to check given string palindrome or not
      def __init__(self,word):
          self.word = word
          self.queue = Queue()
          self.stack = Stack()
     
      def check_palindrome(self):
          for letter in self.word:
              self.queue.push(letter)
              self.stack.push(letter) 
          for i in range(len(self.word)):
              if self.queue.pop != self.stack.pop():
                     return False
          return True
#function call

if __name__ == '__main__':
   s=input("Enter string:")
   result = Palindrome_checker(s)
   if result.check_palindrome():
       print("Given string is palindrome", s)
   else:
       print("Given string is not palindrome", s)
