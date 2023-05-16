


dec1={1:{"name":"p1","age":22},2:{"name":"p2","age":27}}


for key,value in dec1.items(): 
    if int(value["age"])>22:
        print(value["name"])
        
#Another solution
        
for key in dec1:
    x=dec1[key]["age"]
    if(x>22):
        print(dec1[key]["name"])