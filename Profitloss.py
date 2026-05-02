actualcost= float(input ("enter your amount"))
saleamount= float(input ("enter your sale price"))
if (saleamount > actualcost):
    print ("profit")
    profit= saleamount - actualcost
else:
    loss= actualcost - saleamount
    print ("loss")
