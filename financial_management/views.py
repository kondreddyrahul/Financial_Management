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
#def print_vars():
#    print user_name
#    print user_id1
#    print tot_bal1
#    print mf_bal1
#    print po_bal1
#    print fo_bal1
#    print nw_bal1

def login_page(request):
    return render_to_response("login.html") 

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
          # print_vars()
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
          # print_vars()
            return render_to_response("accountpage.html",{"user_id1":user_id1 ,  "mf_bal1":mf_bal1 , "tot_bal1":tot_bal1 , "po_bal1":po_bal1 ,"fo_bal1": fo_bal1, "user_name":user_name,"nw_bal1":nw_bal1})
        except account.DoesNotExist:
            return HttpResponseRedirect("/cooperative_Bank/")
 
##if view is MF show him MF page ,IPO show ipo.htm, FO fo.html else error
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
    for mf in mf_list:
     i=i+1
     mfid = request.POST["abc"+str(i)]
     quantity = request.POST["abcd"+str(i)]
     quantity1= request.POST["pqrs"+str(i)]
     if quantity!="":
      p = MutualFund.objects.get(pk=mfid)
      price=int(p.mf_cost)
      total=price*int(quantity)
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
      # print_vars()  
        c=Transaction(user.user_id,"mf"+str(mc),mfid,total,quantity)
        c.save()
        c=Transaction.objects.all()
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
        
    return render_to_response('Thank.html',{'fo_list':fo_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "fo_bal1":fo_bal1 ,"nw_bal1":nw_bal1,"user_id1":user_id1,"total":total,"counter":counter,"mf_bal1":mf_bal1,"quantity":quantity,"c":c})

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
     if quantity!="":
      p = IPO.objects.get(pk=mfid)
      price=int(p.ipo_cost)
      total=price*int(quantity)
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
            mc = Transaction.objects.count()
            c=Transaction(user.user_id,"ipo"+str(mc),mfid,total,-int(quantity1))
            c.save()
            c=Transaction.objects.all()        
    return render_to_response('Thank1.html',{'fo_list':fo_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "fo_bal1":fo_bal1 ,"nw_bal1":nw_bal1,"user_id1":user_id1,"total":total,"counter":counter,"mf_bal1":mf_bal1})
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
    return render_to_response('Thank2.html',{'fo_list':fo_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "fo_bal1":fo_bal1 ,"nw_bal1":nw_bal1,"user_id1":user_id1,"total":total,"counter":counter,"mf_bal1":mf_bal1})
#mf_id = "MF2008X1";
  #mf = MutualFund.objects.get(pk=mf_id)
  #mf_id1 = mf.mf_ID
  #mf_name1 = mf.mf_Name
  #mf_qty1 = mf.mf_Qty
  #mf_cost1 = mf.mf_cost
  #return render_to_response("mf.html",{"mf_id1":mf_id1,  "mf_name1":mf_name1, "mf_qty1":mf_qty1, "mf_cost1":mf_cost1 })

  
#
#
##change his account balance and clear that get_balance to 0
#def the_last_supper :
