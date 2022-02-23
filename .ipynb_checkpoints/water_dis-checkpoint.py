#this program is to find water displacement due to temperature rise and decrease
from math import *
h1=float(input("enter height of water"))
D1=float(input("enter diameter of upper water sur"))
d1=float(input("enter diameter of lower water sur"))
R1=D1/2
r1=d1/2
a1=(pi*h1*(R1**2+r1**2+R1*r1))/3
print(a1)
h2=float(input("enter height of water"))
D2=float(input("enter diameter of upper water sur"))
d2=float(input("enter diameter of lower water sur"))
R2=D2/2
r2=d2/2
a2=(pi*h2*(R2**2+r1**2+R2*r1))/3
print(a2)
h_dis=a1-a2
print("difference between volume",h_dis)
T=float(input("enter temperature"))
T1=float(input("enter current temp"))
if h_dis>0:

    evo=h_dis/T
    print("evoprated per T",evo)
    ac_evo=T1*evo
    print("evoprated now",ac_evo)
if h_dis<=0 and T1 in range(0,25):
    e=abs(h_dis)
    cool=e/T
    print("water gained on cooling per T",cool)
