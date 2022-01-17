def Display_Array(Array, k): 
    for i in range(k): 
        print(Array[i], end = " ") 
      
def Hashing(Table, Table_Size, Array, Numbers): 
    for i in range(Numbers):           
        HV = Array[i] % Table_Size   
        if (Table[HV] == -1): 
            Table[HV] = Array[i]               
        else: 
            for j in range(Table_Size): 
                table = (HV + j * j) % Table_Size 
                if (Table[table] == -1): 
                    Table[table] = Array[i] 
                    break
    Display_Array(Table, Numbers) 

Array = [23, 5, 56, 87, 98, 77, 222] 
Numbers = 7
Hash_Table_Size = 7 
Original = [0] * 7
for i in range(Hash_Table_Size): 
    Original[i] = -1 
Hashing(Original, Hash_Table_Size, Array, Numbers) 