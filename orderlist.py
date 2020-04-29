fname = input("enter file name")
fh = open(fname)
lst = list()
for line in fh:
    word = line.rstrip().split()
    for element in word:
        if element in lst:
           continue
        else:
          lst.append(element)
new_lst=[int(i) for i in lst]
new_lst.sort()
#modified list
print("modified list: " + str(new_lst))

search = int(input("enter value"))

def binarysearch(value,new_lst,low,high):
    if low > high:
       return False
    mid = (low + high) // 2
    if value == new_lst[mid]:
        return True
    elif value > new_lst[mid]:
         return binarysearch(value,new_lst,mid + 1,high)
    
    elif value < new_lst[mid]:
         return binarysearch(value,new_lst,low,mid - 1)


if binarysearch(search,new_lst,0,len(new_lst)):
    new_lst.remove(search)
else:
    new_lst.append(search)


new_lst.sort()
print(new_lst)
