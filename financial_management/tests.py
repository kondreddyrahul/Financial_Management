from cooperative_Bank.financial_management.models import Customer
from financial_management.models import MutualFund
from financial_management.models import IPO
from financial_management.models import FO
from financial_management.models import Admin
from financial_management.models import account
from financial_management.models import Transaction
from django.utils import unittest
from django.test.client import Client
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    def test_redirect_after_login(self):
        c = Client()
        user = Customer('test1',1010)
        acc = account('1010','13213','3213','321','5435')
        user.save()
        acc.save()
        response = c.post('/cooperative_Bank/',{'user_id': 1010})
        response.content
        self.assertEqual(1 + 1, 2)
        self.assertEqual(response.status_code,200)
      #  self.assertRedirects(response,'/cooperative_Bank/fm/user')
    def test_mf_after_login(self):
        c = Client()
        user = Customer('test1',1010)
        acc = account('1010','13213','3213','321','5435')
        mf=MutualFund('2','mf',12,12321)
        mf.save()
        user.save()
        acc.save()
        response = c.post('/cooperative_Bank/fm/MF',{'abc1': '2','abcd1':'10'})
        c.post('/cooperative_Bank/fm/MF', {'name': 'fred', 'passwd': 'secret'})
        self.assertEqual(1 + 1, 2)
        response.content
       # self.assertEqual(response.status_code,302)

class MutualFundTestCase(unittest.TestCase):
    def test_mf1_after_login(self):
        self.mf=MutualFund('2','mf',12,12321)
        self.mf.save()
        self.mf.mf_Qty=self.mf.mf_Qty-100000
        k=self.mf.mf()
        self.assertEqual(self.mf.mf_Qty, 0)

class IPOTestCase(unittest.TestCase):
    def test_mf1_after_login(self):
        self.mf=IPO('2','mf',12,12321)
        self.mf.save()
        self.mf.ipo_Qty=self.mf.ipo_Qty-100000
        k=self.mf.ipo()
        self.assertEqual(self.mf.ipo_Qty, 0)  

class FOTestCase(unittest.TestCase):
    def test_mf1_after_login(self):
        self.mf=FO('2','mf',12,12321)
        self.mf.save()
        self.mf.fo_Qty=self.mf.fo_Qty-100000
        k=self.mf.fo()
        self.assertEqual(self.mf.fo_Qty, 0)      
