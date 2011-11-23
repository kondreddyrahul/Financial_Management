##@author:ashish
from django.db import models
import json
##@param:Customer who are identified by their id and name

class Customer(models.Model):
  customer_Name = models.CharField(max_length=200)
## Customer is uniquely identified by his/her id
  customer_ID = models.CharField(max_length=10, primary_key = True)
  def __unicode__(self):
        return self.customer_ID
##For each customer there is an account along with all his bank details.
##@param:Identified by user id.
class account(models.Model):
##Each account has a primary key customers id.
    user_id =models.ForeignKey(Customer, primary_key = True)
##Total Balance: Gives information of the total balance in an account.It includes all the other balances.It is the summation of balances of mutual Fund,IPO Funds etc.
    tot_bal =models.CharField(max_length=30)
##Balance which we have allocated to Mutual Funds. If we want to buy MF, then we need to add money in this from the total balance
    mf_bal =models.CharField(max_length=30)
##Balance which we have allocated to IPO Funds. If we want to buy IPO, then we need to add money in this from the total balance 
    po_bal =models.CharField(max_length=30)
##Balance which we have allocated to FO Funds. If we want to buy FO, then we need to add money in this from the total balance
    fo_bal =models.CharField(max_length=30)

##Models list of mutual funds available along with their quantity available and cost.
class MutualFund(models.Model):
## Each Mutual Fund identified by its unique mutual fund id.
  mf_ID = models.CharField(max_length=10, primary_key = True)
  mf_Name = models.CharField(max_length=200)
## Cost of each mutual fund entity.
  mf_cost = models.DecimalField(max_digits=10, decimal_places=2)
## Total Quantity available in the market. Keeps on reducing on transaction of buy and reduces on transaction of sell.
  mf_Qty = models.IntegerField()
  def __unicode__(self):
        return self.mf_Name
##Function used for unit testing of Mutual Funds to see that the value does not go below 0 .
  def mf(self): 
      if self.mf_Qty<0:
          self.mf_Qty=0
          return self.mf_Qty
##List of IPO available along with their quantity available and cost.  
class IPO(models.Model):
  ipo_Name = models.CharField(max_length=200)
## Each Mutual Fund identified by its unique IPO id.
  ipo_ID = models.CharField(max_length=10, primary_key = True)
## Total Quantity available in the market. Keeps on reducing on transaction of buy and reduces on transaction of sell.
  ipo_cost = models.DecimalField(max_digits=10, decimal_places=2)
  ipo_Qty = models.IntegerField()
  def __unicode__(self):
        return self.ipo_Name
  def ipo(self): 
      if self.ipo_Qty<0:
          self.ipo_Qty=0
          return self.ipo_Qty
##List of FO available along with their quantity available and cost.      
class FO(models.Model):
  fo_Name = models.CharField(max_length=200)
## Each Mutual Fund identified by its unique FO id.
  fo_ID = models.CharField(max_length=10,primary_key = True)
  fo_cost = models.DecimalField(max_digits=10, decimal_places=2)
## Total Quantity available in the market. Keeps on reducing on transaction of buy and reduces on transaction of sell.
  fo_Qty = models.IntegerField()
  def __unicode__(self):
        return self.fo_Name
  def fo(self): 
      if self.fo_Qty<0:
          self.fo_Qty=0
          return self.fo_Qty
## All the transactions made with the bank by all the customers.Used to determine the transaction table for a particular customer.      
class Transaction(models.Model):
  transaction_user = models.ForeignKey(Customer)
## Each Transaction is identified by its transaction id.
  transaction_id = models.CharField(max_length=10, primary_key = True)
  transaction_trans = models.CharField(max_length=10) 
  transaction_total = models.DecimalField(max_digits=10, decimal_places=2)
## Total quantity bought or sold thuscan be positive or negative respectively.  
  transaction_Quantity = models.IntegerField()
  def __unicode__(self):
        return self.transaction_id
    ##Admin incharge of opening and closing of accounts .
class Admin(models.Model):
  admin_Name = models.CharField(max_length=200)
  admin_ID = models.CharField(max_length=10, primary_key = True)
  def __unicode__(self):
        return self.admin_ID
