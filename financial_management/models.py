from django.db import models
import json
#Customer who are identified by their id and name
class Customer(models.Model):
  customer_Name = models.CharField(max_length=200)
  customer_ID = models.CharField(max_length=10, primary_key = True)
  def __unicode__(self):
        return self.customer_ID
#For each customer there is an account along with all his bank details
class account(models.Model):
    user_id =models.ForeignKey(Customer, primary_key = True)
    tot_bal =models.CharField(max_length=30)
    mf_bal =models.CharField(max_length=30)
    po_bal =models.CharField(max_length=30)
    fo_bal =models.CharField(max_length=30)

#list of mutual funds available along with their quantity available and cost.
class MutualFund(models.Model):
  mf_ID = models.CharField(max_length=10, primary_key = True)
  mf_Name = models.CharField(max_length=200)
  mf_cost = models.DecimalField(max_digits=10, decimal_places=2)
  mf_Qty = models.IntegerField()
  def __unicode__(self):
        return self.mf_Name
  def mf(self): 
      if self.mf_Qty<0:
          self.mf_Qty=0
          return self.mf_Qty
#list of IPO available along with their quantity available and cost.  
class IPO(models.Model):
  ipo_Name = models.CharField(max_length=200)
  ipo_ID = models.CharField(max_length=10, primary_key = True)
  ipo_cost = models.DecimalField(max_digits=10, decimal_places=2)
  ipo_Qty = models.IntegerField()
  def __unicode__(self):
        return self.ipo_Name
  def ipo(self): 
      if self.ipo_Qty<0:
          self.ipo_Qty=0
          return self.ipo_Qty
#list of FO available along with their quantity available and cost.      
class FO(models.Model):
  fo_Name = models.CharField(max_length=200)
  fo_ID = models.CharField(max_length=10,primary_key = True)
  fo_cost = models.DecimalField(max_digits=10, decimal_places=2)
  fo_Qty = models.IntegerField()
  def __unicode__(self):
        return self.fo_Name
  def fo(self): 
      if self.fo_Qty<0:
          self.fo_Qty=0
          return self.fo_Qty
#All the transactions made with the bank by all the customers.Used to determine the transaction table for a particular customer.      
class Transaction(models.Model):
  transaction_user = models.ForeignKey(Customer)
  transaction_id = models.CharField(max_length=10, primary_key = True)
  transaction_trans = models.CharField(max_length=10) 
  transaction_total = models.DecimalField(max_digits=10, decimal_places=2)
  transaction_Quantity = models.IntegerField()
  def __unicode__(self):
        return self.transaction_id
    
class Admin(models.Model):
  admin_Name = models.CharField(max_length=200)
  admin_ID = models.CharField(max_length=10, primary_key = True)
  def __unicode__(self):
        return self.admin_ID
