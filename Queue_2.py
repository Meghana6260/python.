def enQueue(Q, ele):
    Q.append(ele)
    print(ele, " is inserted into Q")
 
def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return 
    ele = Q.pop(0)
    print("Deleted element is", ele)
 
def printQueue(Q):
    if len(Q) == 0:
        print("Nothing is present in Q")
        return 
    print(Q)
 
def queueempty(Q):
    if len(Q)==0:
        print("Queue is empty")
    else:
        print("Queue is not empty")
def frontnode(Q):
    if len(Q)==0:
        print("Queue is empty")
        return
    print(Q[0])
    
Q = []
n = int(input().strip())
while n > 0:
   word = list(map(int, input().split()))
   l = word[0]
   if l == 1:
       num = word[1]
       Q.append(num)
       print(num, "inserted")
   elif l == 2:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print(Q[0])
   elif l == 3:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print(Q[0])
           Q.pop(0)
   elif l == 4:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           for ele in Q:
               print(ele, end = " ")
           print()
   else:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print("Queue is not empty")
      
   n -= 1
   
    
        
