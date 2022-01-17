class Hash_Table:
    def __init__(self, Array_Size):
        self.Array_Size = Array_Size
        self.Array = [[] for i in range(self.Array_Size)]

    def Length_Array(self):
        Count = 0
        for i in self.Array:
            if i != None:
                Count += 1
        return Count
    
    def Hashing(self, value):
        mod = value % self.Array_Size
        return mod

    def Insert(self, Array ,Key_value, value): 
        Hash_Key = self.Hashing(Key_value) 
        Array[Hash_Key].append(value) 
 
    def Display_Hash(self,HashTable):      
        for i in range(len(HashTable)): 
            print(i, end = " ") 
            for j in HashTable[i]: 
                print("->", end = " ") 
                print(j, end = " ")    
            print() 

Table=Hash_Table(12)
Table.Insert(Table.Array,5, 'Karachi') 
Table.Insert(Table.Array,66, 'Lahore') 
Table.Insert(Table.Array,34, 'Peshawar') 
Table.Insert(Table.Array,23, 'Quetta') 
Table.Insert(Table.Array,78, 'Rawalpindi') 
Table.Insert(Table.Array,55, 'Kashmir') 
Table.Display_Hash (Table.Array) 
