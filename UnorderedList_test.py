class Node:

    def __init__(self,initdata):

        self.data = initdata

        self.next = None

    def getData(self):

        return self.data

    def getNext(self):

         return self.next

    def setData(self,newdata):

        self.data = newdata

    def setNext(self,newnext):

        self.next = newnext

class UnorderedList:

    def __init__(self):

        self.head = None

    def isEmpty(self):

        return self.head == None

    def add(self,item):

        temp = Node(item)

        temp.setNext(self.head)

        self.head = temp

    def size(self):

        current = self.head

        count = 0

        while current != None:

            count = count + 1

            current = current.getNext()

        return count

    def search(self,item):

        current = self.head

        found = False

        while current != None and not found:

            if current.getData() == item:

                found = True

            else:

                current = current.getNext()

        return found

    def remove(self,item):

        current = self.head

        previous = None

        found = False

        while not found:

            if current.getData() == item:

                found = True

            else:

                previous = current

                current = current.getNext()

        if previous == None:

            self.head = current.getNext()

        else:

            previous.setNext(current.getNext())
    
    def print_list(self):
        
        test = self.head  
        if(test==None):
          element in list 
          print("[]")

        else:    
            print("[",end="")
            while test.next is not None:
                print(test.data,end=",")
                test = test.next
            print(test.data,"]",sep="")

    def element_at(self, position):
        
        if position >0 and position<self.size()-1: 
            test=self.head  
            count =0
            while count!=position: 
                test=test.next
                count+=1
            return test.data   

    def insert(self,data,position):
        
        if position==0:   

            newnode = Node(data)
            newnode.setNext(self.head) 
            self.head =newnode   
        elif position>0 and position<self.size()-1:
            test= self.head
            count=1
            while count!=position: 
                test=test.getNext() 
                count+=1
            newnode=Node(data)
            newnode.setNext(test.getNext()) 
            test.setNext(newnode) 

    def swap(self,pos1,pos2):
        count=0
        test1=self.head  
        test2=self.head
        if pos1<=self.size()-1 and pos2<=self.size()-1: 
            while count<pos1 or count <pos2:  
                if(count<pos1):
                    test1=test1.getNext()
                if(count<pos2):
                    test2=test2.getNext()
                count+=1
            temp = test1.data
            test1.data = test2.data
            test2.data = temp

    def value_repeats(self):
        if(self.size()<2):
            return False
        else:
            data = self.head.data
            test= self.head
            while test.next is not None:
                if data == test.next.data:
                    return True
                test=test.getNext()
                data=test.getData()
            return False


