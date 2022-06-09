from matplotlib import pyplot as pt
def compoundint(p,r,t):
    lst=[]
    x=[]
    for i in range(1,n+1):
        x.append(i)
        a=p*(1+(r/100))**(i*t)
        ci=a-p
        lst.append(ci)
    pt.plot(x,lst)
    return ci
    
p = input("Enter the principal ")
r= input("Enter the interest rate ")
t= input("Enter the number of years ")
n=input("enter the compund interest")
print("compound interest is",compoundint(p,r,t))
