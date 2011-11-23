# Create your views here.
from django.shortcuts import render_to_response
from cooperative_Bank.financial_management.models import account
from cooperative_Bank.financial_management.models import Customer
from cooperative_Bank.financial_management.models import MutualFund
from cooperative_Bank.financial_management.models import IPO
from cooperative_Bank.financial_management.models import FO
from cooperative_Bank.financial_management.models import Transaction
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
user_name = None
user_id1 = None
tot_bal1= None
mf_bal1= None
po_bal1= None
fo_bal1= None
nw_bal1= None
mfid=None
p=None
counter=None
quantity=None
price=None
total=None
ic=0
mc=0
c=None
##Login page is use to check if the id provided is valid and gives the personal details page if the id is correct.
def login_page(request):
    return render_to_response("login.html") 
## This page provides information about the amount alloted to Mutual Funds, IPO, FO .account_detail also tells us the total balance available to the customer.
 ##@return:Details of the Account-if the id correct then displays the personal details such total balance, mutual fund balance from the account daatabase.   account_detail also provides the option of changing amount allocated to each of the types such as MF balance, IPO Balance etc.lot of testing has been done for this part and after all the testing javascript and form validation was incorporated in the code.   
def account_detail(request):
    if 'temp_MF' in request.POST and request.POST['temp_MF']:
        user_id = request.POST["user_id"]
        temp_mf = request.POST["temp_MF"]
        temp_po = request.POST["temp_PO"]
        temp_fo = request.POST["temp_FO"]
        print(user_id)
        print(temp_mf)
        try:
            
            global user_name
            global user_id1 
            global tot_bal1
            global mf_bal1
            global po_bal1
            global fo_bal1
            global nw_bal1
            
            user = account.objects.get(pk=user_id)
            customer = Customer.objects.get(pk=user_id)
            user_name = customer.customer_Name
            user_id1 = user.user_id
            tot_bal1= int(user.tot_bal)
            mf_bal1= int(user.mf_bal) +int(temp_mf)
            po_bal1= int(user.po_bal)+int(temp_po)
            fo_bal1= int(user.fo_bal)+int(temp_fo)
            nw_bal1 =(tot_bal1)-(mf_bal1+po_bal1+fo_bal1)
            user.fo_bal=fo_bal1
            user.mf_bal=mf_bal1
            user.po_bal=po_bal1
            user.tot_bal=tot_bal1
            user.save()
          
            return render_to_response("accountpage.html",{"user_id1":user_id1 ,  "mf_bal1":mf_bal1 , "tot_bal1":tot_bal1 , "po_bal1":po_bal1 ,"fo_bal1": fo_bal1, "user_name":user_name,"nw_bal1":nw_bal1})
        except account.DoesNotExist:
            return HttpResponseRedirect("/cooperative_Bank/")
 
      
    else:
        user_id = request.POST["user_id"]
        try:
            
            global user_name
            global user_id1 
            global tot_bal1
            global mf_bal1
            global po_bal1
            global fo_bal1
            global nw_bal1
            
            user = account.objects.get(pk=user_id)
            customer = Customer.objects.get(pk=user_id)
            user_name = customer.customer_Name
            user_id1 = user.user_id
            tot_bal1= int(user.tot_bal)
            mf_bal1= int(user.mf_bal)
            po_bal1= int(user.po_bal)
            fo_bal1= int(user.fo_bal)
            nw_bal1 =(tot_bal1)-(mf_bal1+po_bal1+fo_bal1)
         
            return render_to_response("accountpage.html",{"user_id1":user_id1 ,  "mf_bal1":mf_bal1 , "tot_bal1":tot_bal1 , "po_bal1":po_bal1 ,"fo_bal1": fo_bal1, "user_name":user_name,"nw_bal1":nw_bal1})
        except account.DoesNotExist:
            return HttpResponseRedirect("/cooperative_Bank/")
 
##If view is MF show him MF page ,IPO show ipo.htm, FO fo.html else errorThis page shows the list of all the Mutual Funds available in the market along with their prices and quantity floated in the market
def mf_detail(request):
    global user_name
    global user_id1 
    global tot_bal1
    global mf_bal1
    global po_bal1
    global fo_bal1
    global nw_bal1
    global mfid
    global p
    counter = 0
    mf_list = MutualFund.objects.all()
    return render_to_response('mf.html',{'mf_list':mf_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "mf_bal1":mf_bal1 ,"nw_bal1":nw_bal1,"mfid":mfid,"p":p,"counter":counter})
##This page shows the list of all the IPO available in the market along with their prices and quantity floated in the market
def ipo_detail(request):
    global user_name
    global user_id1 
    global tot_bal1
    global mf_bal1
    global po_bal1
    global fo_bal1
    global nw_bal1

    ipo_list = IPO.objects.all()
    return render_to_response('ipo.html',{'ipo_list':ipo_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "po_bal1":po_bal1 ,"nw_bal1":nw_bal1,})
##This page shows the list of all the FO available in the market along with their prices and quantity floated in the market
def fo_detail(request):
    global user_name
    global user_id1 
    global tot_bal1
    global mf_bal1
    global po_bal1
    global fo_bal1
    global nw_bal1

    fo_list = FO.objects.all()
    return render_to_response('fo.html',{'fo_list':fo_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "fo_bal1":fo_bal1 ,"nw_bal1":nw_bal1,})
##Checks to see if quantity entered is correct in all respects and if true then the transaction is done. This part involves the major part of the testing like validating the quantity is less than available, amount in the balance is greater than the amount to be used in transaction and if it is true then the transaction of mutual fund is done for a particular customer.
 ##We can simultaneously buy /sell more than one product depending on the balance.
##if he has entered some quantity in buy then check if it is feasible.
##If quantity asked by him is less than available and his balance in Mutual Fund is greater than the cost of acquisition then he can buy.
##Sell option was added in Phase 2 of our project in which customer was provided with the option of selling the MF he is currently holding.
def thank_detail(request):
    global user_name
    global user_id1 
    global tot_bal1
    global mf_bal1
    global po_bal1
    global fo_bal1
    global nw_bal1
    global mfid
    global quantity
    global price
    global total
    global mc
    global c
    i=0
    counter=0
    user = account.objects.get(pk=user_id1)
    mfid = request.POST["abc1"]
    p = MutualFund.objects.get(pk=mfid)
    mf_list = MutualFund.objects.all()
    fo_list = FO.objects.all()
  ##We can simultaneously buy /sell more than one product depending on the balance.
    for mf in mf_list:
     i=i+1
     mfid = request.POST["abc"+str(i)]
     quantity = request.POST["abcd"+str(i)]
     quantity1= request.POST["pqrs"+str(i)]
    #if he has entered some quantity in buy then check if it is feasible
     if quantity!="":
      p = MutualFund.objects.get(pk=mfid)
      price=int(p.mf_cost)
      total=price*int(quantity)
      #If quantity asked by him is less than available and his balance in Mutual Fund is greater than the cost of acquisition then he can buy
      if int(quantity)<=int(p.mf_Qty):
       if total<=mf_bal1:
        c=Transaction.objects.all()
        mc = Transaction.objects.count()
        user.mf_bal=int(user.mf_bal)-total
        user.tot_bal=int(user.tot_bal)-total
        user.save()
        p.mf_Qty=int(p.mf_Qty)-int(quantity)
        p.save()
        counter=1
        mf_bal1=user.mf_bal 
        tot_bal1=user.tot_bal
        nw_bal1 =(tot_bal1)-(mf_bal1+po_bal1+fo_bal1)
     #Transaction table is updated .
        c=Transaction(user.user_id,"mf"+str(mc),mfid,total,quantity)
        c.save()
        c=Transaction.objects.all()
      #else:
       #   return HttpResponseRedirect("/cooperative_Bank/fm/MF")  
      #Sell option was added in Phase 2 of our project in which customer was provided with the option of selling the MF he is currently holding
     if quantity1!="":
         co=0;
         c = Transaction.objects.filter(transaction_user=user_id1)
         p = MutualFund.objects.get(pk=mfid)
         price=int(p.mf_cost)
         for j in c:
            if j.transaction_trans==mfid:
                co=co+j.transaction_Quantity
         if int(quantity1)<co:
            total=price*int(quantity1)
            user.mf_bal=int(user.mf_bal)+total
            user.tot_bal=int(user.tot_bal)+total
            user.save()
            p.mf_Qty=int(p.mf_Qty)+int(quantity1)
            p.save()
            counter=1
            mf_bal1=user.mf_bal 
            tot_bal1=user.tot_bal
            nw_bal1 =(tot_bal1)-(mf_bal1+po_bal1+fo_bal1)
            # print_vars()  
            c=Transaction(user.user_id,"mf"+str(mc),mfid,total,-int(quantity1))
            c.save()
            c=Transaction.objects.all()
         #else:
        #  return HttpResponseRedirect("/cooperative_Bank/fm/MF")
    return render_to_response('Thank.html',{'fo_list':fo_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "fo_bal1":fo_bal1 ,"nw_bal1":nw_bal1,"user_id1":user_id1,"total":total,"counter":counter,"mf_bal1":mf_bal1,"quantity":quantity,"c":c})
##checks to see if quantity entered is correct in all respects and if true then the transaction is done. This part involves the major part of the testing like validating the quantity is less than available, amount in the balance is greater than the amount to be used in transaction and if it is true then the transaction of IPO is done for a particular customer
def thank1_detail(request):
    global user_name
    global user_id1 
    global tot_bal1
    global mf_bal1
    global po_bal1
    global fo_bal1
    global nw_bal1
    global mfid
    global quantity
    global price
    global total
    global ic
    i=0
    counter=0
    user = account.objects.get(pk=user_id1)
    mfid = request.POST["abc1"]
    p = IPO.objects.get(pk=mfid)
    ipo_list = IPO.objects.all()
    fo_list = FO.objects.all()
    for ipo in ipo_list:
     i=i+1
     mfid = request.POST["abc"+str(i)]
     quantity = request.POST["abcd"+str(i)]
     quantity1= request.POST["pqrs"+str(i)]
     #if he has put some quantity in buy
     if quantity!="":
      p = IPO.objects.get(pk=mfid)
      price=int(p.ipo_cost)
      total=price*int(quantity)
      #Quantity asked is less than available
      if int(quantity)<=int(p.ipo_Qty):
       if total<=po_bal1:
        user.po_bal=int(user.po_bal)-total
        user.tot_bal=int(user.tot_bal)-total
        user.save()
        counter=1
        p.ipo_Qty=int(p.ipo_Qty)-int(quantity)
        p.save()
        po_bal1=user.po_bal
        tot_bal1=user.tot_bal
        nw_bal1 =(tot_bal1)-(mf_bal1+po_bal1+fo_bal1)
        mc = Transaction.objects.count()
        c=Transaction(user.user_id,"ipo"+str(mc),mfid,total,quantity)
        c.save()
        c=Transaction.objects.all()
    #  else:
     #     return HttpResponseRedirect("/cooperative_Bank/fm/IPO")
     if quantity1!="":
         co=0;
         c = Transaction.objects.filter(transaction_user=user_id1)
         p = IPO.objects.get(pk=mfid)
         price=int(p.ipo_cost)
         for j in c:
            if j.transaction_trans==mfid:
                co=co+j.transaction_Quantity
         if int(quantity1)<co:
            total=price*int(quantity1)
            user.po_bal=int(user.po_bal)+total
            user.tot_bal=int(user.tot_bal)+total
            user.save()
            counter=1
            p.ipo_Qty=int(p.ipo_Qty)+int(quantity1)
            p.save()
            po_bal1=user.po_bal
            tot_bal1=user.tot_bal
            nw_bal1 =(tot_bal1)-(mf_bal1+po_bal1+fo_bal1)
            #If transaction is possible then they are saved in the transaction table database.
            mc = Transaction.objects.count()
            c=Transaction(user.user_id,"ipo"+str(mc),mfid,total,-int(quantity1))
            c.save()
            c=Transaction.objects.all()
      #   else:
       #   return HttpResponseRedirect("/cooperative_Bank/fm/IPO")           
    return render_to_response('Thank1.html',{'fo_list':fo_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "fo_bal1":fo_bal1 ,"nw_bal1":nw_bal1,"user_id1":user_id1,"total":total,"counter":counter,"mf_bal1":mf_bal1})
##Displays the transaction table for a particular customer who is logged in the session.It shows all the buy (+) and sell (-) transactions along with the quantity, total cost and name of the MF, IPO or FO. 
def trans_detail(request):
    global user_name
    global user_id1 
    global tot_bal1
    global mf_bal1
    global po_bal1
    global fo_bal1
    global nw_bal1
    global mfid
    global quantity
    global price
    global total
    global ic
    global p 
    user = account.objects.get(pk=user_id1)
    ic=user.user_id
    p = Transaction.objects.filter(transaction_user=ic)
    p = Transaction.objects.all()
    return render_to_response('Trans.html',{"user_name":user_name ,"tot_bal1":tot_bal1 , "fo_bal1":fo_bal1 ,"nw_bal1":nw_bal1,"user_id1":user_id1,"total":total,"counter":counter,"mf_bal1":mf_bal1,"p":p})
## Checks to see if quantity entered is correct in all respects and if true then the transaction is done. This part involves the major part of the testing like validating the quantity is less than available, amount in the balance is greater than the amount to be used in transaction and if it is true then the transaction of IPO is done for a particular customer
def thank2_detail(request):
    global user_name
    global user_id1 
    global tot_bal1
    global mf_bal1
    global po_bal1
    global fo_bal1
    global nw_bal1
    global mfid
    global quantity
    global price
    global total
    i=0
    counter=0
    user = account.objects.get(pk=user_id1)
    fo_list = FO.objects.all()
    for fo in fo_list:
     i=i+1
     mfid = request.POST["abc"+str(i)]
     quantity = request.POST["abcd"+str(i)]
     quantity1= request.POST["pqrs"+str(i)]
     if quantity!="":
      p = FO.objects.get(pk=mfid)
      price=int(p.fo_cost)
      total=price*int(quantity)
      #if quantity asked of FO is less than that available then go on.
      if int(quantity)<=int(p.fo_Qty):
       if total<=mf_bal1:
        user.fo_bal=int(user.fo_bal)-total
        user.tot_bal=int(user.tot_bal)-total
        user.save() 
        counter=1
        fo_bal1=user.fo_bal   
        tot_bal1=user.tot_bal
        nw_bal1 =(tot_bal1)-(mf_bal1+po_bal1+fo_bal1)
        p.fo_Qty=int(p.fo_Qty)-int(quantity)
        p.save()
        mc = Transaction.objects.count()
        c=Transaction(user.user_id,"FO"+str(mc),mfid,total,quantity)
        c.save()
        c=Transaction.objects.all()
      #else Return to the FO list page.
   #   else:
    #      return HttpResponseRedirect("/cooperative_Bank/fm/FO")  
     if quantity1!="":
         co=0;
         c = Transaction.objects.filter(transaction_user=user_id1)
         p = FO.objects.get(pk=mfid)
         price=int(p.fo_cost)
         for j in c:
            if j.transaction_trans==mfid:
                co=co+j.transaction_Quantity
         if int(quantity1)<co:
            total=price*int(quantity1)
            user.fo_bal=int(user.fo_bal)+total
            user.tot_bal=int(user.tot_bal)+total
            user.save() 
            counter=1
            fo_bal1=user.fo_bal   
            tot_bal1=user.tot_bal
            nw_bal1 =(tot_bal1)-(mf_bal1+po_bal1+fo_bal1)
            p.fo_Qty=int(p.fo_Qty)+int(quantity1)
            p.save()
            mc = Transaction.objects.count()
            c=Transaction(user.user_id,"FO"+str(mc),mfid,total,-int(quantity))
            c.save()
            c=Transaction.objects.all()        
     #    else:
      #    return HttpResponseRedirect("/cooperative_Bank/fm/FO") 
    return render_to_response('Thank2.html',{'fo_list':fo_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "fo_bal1":fo_bal1 ,"nw_bal1":nw_bal1,"user_id1":user_id1,"total":total,"counter":counter,"mf_bal1":mf_bal1})

