class Queue:
  def __init__(self):
      self.balance = 0
      print("welcome to banking")
  
  def enqueue_deposit(self):
      amount = float(input("enter the amount to deposit: "))
      self.balance += amount
      print("\nAmount deposited: ", amount)

  def enqueue_withdraw(self):
      amount = float(input("enter the amount to withdraw: "))
      if self.balance >= amount:
          self.balance -= amount
          print("\nyou withrdaw: ",amount)
      else:
          print("insuffient balance")

  def queue_display(self):
      print("\n Avalible balance:", self.balance)
  
  def queue_exit(self):
      exit()

if __name__ == '__main__':
   q = Queue()
   try:
      while True:
            print("Please Enter the option that you want to make transaction") 
            n = int(input("1. Deposite\n  2.withdraw\n 3.display amount\n 4. cancel transaction\n"))
            if n == 1:
                q.enqueue_deposit()
            elif n == 2:
                 q.dequeue_withdraw()
            elif n == 3:
                 q.queue_display()
            
            elif n == 4:
                   q.queue_exit()

   except ValueError:
          print("please enter valied option")
