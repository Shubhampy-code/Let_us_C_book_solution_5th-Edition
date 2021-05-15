"""When interest compounds q times per year at an annual rate of
r % for n years, the principle p compounds to an amount a as per
the following formula
a = p ( 1 + r / q ) nq
Write a program to read 10 sets of p, r, n & q and calculate
the corresponding as."""
a=0
p=2
r=3
q=2
n=1
while (p<=5) and (r<=6) and (q<=4) and (n<=3):
    a = p * pow(( 1 + r / q ),(n*q))
    print("a = "+str(a) +" for  p = " + str(p)+ ", r = "+str(r)+", q = " + str(q)+" and r = "+str(n) )
    p=p+1
    r=r+1
    q=q+1
    n=n+1
