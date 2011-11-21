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

def login_page(request):
    return render_to_response("login.html")


def account_detail(request):
    user_id = request.POST["user_id"]
    try:
        user = account.objects.get(pk=user_id)
        customer = Customer.objects.get(pk=user_id)
        user_name = customer.customer_Name
        user_id1 = user.user_id
        tot_bal1= user.tot_bal
        mf_bal1= user.mf_bal
        po_bal1= user.po_bal
        fo_bal1= user.fo_bal
        return render_to_response("accountpage.html",{"user_id1":user_id1 ,  "mf_bal1":mf_bal1 , "tot_bal1":tot_bal1 , "po_bal1":po_bal1 ,"fo_bal1": fo_bal1, "user_name":user_name})
    except account.DoesNotExist:
        return HttpResponseRedirect("/cooperative_Bank/")

 
##if view is MF show him MF page ,IPO show ipo.htm, FO fo.html else error
def mf_detail(request):
  mf_list = MutualFund.objects.all()
  return render_to_response('mf.html',{'mf_list':mf_list})

def ipo_detail(request):
  ipo_list = IPO.objects.all()
  return render_to_response('ipo.html',{'ipo_list':ipo_list})
  
def fo_detail(request):
  fo_list = FO.objects.all()
  return render_to_response('fo.html',{'fo_list':fo_list})

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
