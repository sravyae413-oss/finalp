x=int(input("enter a number:"))
sum=0
for a in range(1,x+1):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count=count+1
        if count==2:
            sum=sum+a
print(sum)
print("prime number")
print(count)

            
        
