m=input("enter the month(1-12):")
y=input("enter the year:")
if(m<=12):
    if(y%4==0):
        if(m==2):
            d=29
        else:
            if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
                d=31
            else:
                d=30
    else:
        if(m==2):
            d=28
        else:
            if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
                d=31
            else:
                d=30
    print "number of days in given month:",d
else:
    print "invalid month"
    