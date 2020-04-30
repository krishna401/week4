from PrimeNumber import prime
from stack import Stack
from stack import Node

#create object of stack class
obj = Stack()

#creating object of prime class
prime_obj = prime()

#creating prime anagram list
prime_anagram = []

#creating list of prime number in given range
prime_list = prime_obj.prime(0, 1000)

#checking prime number anagran or not
for num in prime_list:
    if num <= 10:
       continue
    number = prime_obj.anagram(num)
    if prime_obj.prime_check(number) and 0 <= number <= 1000:
        prime_anagram.append(number)
        prime_anagram.append(num)
        prime_list.remove(number)

#finding thr length of prime anagraam list
length =  len(prime_anagram)

#Adding the prime anagram to stack

for number in range(length):
    num = Node(prime_anagam[number])
    obj.push(num)

#printing in reverse order
for number in range (length):
    data = obj.pop()
    print(data, end=" ")
