class Hash_Table:
    def __init__(self, Array_Size):
        self.Array_Size = Array_Size
        self.Array = [None] * self.Array_Size

    def Array_Length(self):
        Count = 0
        for i in self.Array:
            if i != None:
                Count += 1
        return Count

    def Hash(self, Value):
        mod = Value % self.Array_Size
        return mod

    def Insertion(self, Value):
        K_mod = self.Hash(Value)
        Number = K_mod
        while True:
            if self.Array[K_mod] is None:
                self.Array[K_mod] = Value
                return K_mod
            if self.Array[K_mod] == Value:
                return -2
            K_mod = (K_mod + 1) % self.Array_Size
            if K_mod == Number:
                return -1
            
    def Search_Value(self, Value):
        hash = self.Hash(Value)
        if self.Array[hash] is None:
            print('Hash Table is empty')
            return
        for i in range(self.Array_Size):
            mod = (hash + i) % self.Array_Size
            if self.Array[mod] == Value:
                print(mod, self.Array[mod])
                return
        print('Value is not Present in Hash Table')
        return
            
Table = Hash_Table(3)
Table.Insertion(23) 
Table.Insertion(88)
Table.Insertion(70) 
Table.Insertion(34)
Table.Search_Value(23) 
Table.Search_Value(70)
Table.Search_Value(88)
Table.Search_Value(67)