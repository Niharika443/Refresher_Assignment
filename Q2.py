car = {}
x = open("Q2_result.txt","a")
brand_name=list(map(str,input("Enter different brand names of car:").split()))
colour=list(map(str,input("Enter colours of the car:").split()))
print("The brand names of the car are: ",brand_name)
print("The brand names of the car are: ",brand_name,file=x)
print("The colours of the car are: ",colour)
print("The colours of the car are: ",colour,file=x)
car=dict(zip(brand_name,colour))
print("The dictionary is:",car)
print("The dictionary is:",car,file=x)