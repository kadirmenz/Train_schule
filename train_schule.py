def read_journey_lengths(filename):
    filen = open("journey_lengths.txt","r")
    dict_journey = {}
    for i in file:
        dict1 = {}
        (key,key,value) = i.split()
        dict_journey[int(key)] = value
    dict_journey = read_journey_lengths("journey_lengths.txt")
    
    
def  read_train_schedule(filename):
    
    dic= {}
    file= open(filename, "r")
    a=file.readlines()
    b=[]
    for i in range(len(a)):
        spr=a[i].split()
        b.append(spr)    
        
    for each in b:
        
        if each[0] not in dic:
           
            dic[each[0]]= {}  
            
        dic[each[0]].update({each[1]: each[2:]}) 
        
        

    return dic

cities=["Paris" , "London" ,"Amsterdam" ,"Berlin" ,"Brussels" ,"Zurich" ,"Frankfurt"]

def write_to_file (list_of_cities, file_cities):
    writer=open(file_cities , "w")
    for c in list_of_cities:
        writer.write(c)
        writer.write("\n")