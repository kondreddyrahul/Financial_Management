# Create your views here.
from django.shortcuts import render_to_response
from cooperative_Bank.financial_management.models import account
from cooperative_Bank.financial_management.models import Customer
from cooperative_Bank.financial_management.models import MutualFund
from cooperative_Bank.financial_management.models import IPO
from cooperative_Bank.financial_management.models import FO
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse

user_name = None
user_id1 = None
tot_bal1= None
mf_bal1= None
po_bal1= None
fo_bal1= None
nw_bal1= None

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
    mf_list = MutualFund.objects.all()
    return render_to_response('mf.html',{'mf_list':mf_list,"user_name":user_name ,"tot_bal1":tot_bal1 , "mf_bal1":mf_bal1 ,"nw_bal1":nw_bal1})

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
