from piston.handler import BaseHandler
from financial_management.models import Transaction,account
from piston.doc import generate_doc


class FM_Trans_Handler( BaseHandler ):
    allowed_methods = ('GET',)
    model = Transaction
    
    def read(self, request, user_id=0,transaction_id=0):
        if user_id:
            setquer=Transaction.objects.filter(transaction_user=user_id)
            return setquer  
          
        if transaction_id:
            setquer=Transaction.objects.filter(transaction_id=transaction_id)
            return setquer
        else:
            return Transaction.objects.all()

#    def read( self, request, expression ):
#       return eval( expression )
class FM_Bal_Handler(BaseHandler):
   allowed_methods = ('GET',)
   model = account   

   def read(self, request, user_id=0):
       if user_id:
           setquer=account.objects.filter(user_id=user_id)
           return setquer        
       else:
           return account.objects.all()
