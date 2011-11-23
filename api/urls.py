from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import FM_Trans_Handler,FM_Bal_Handler
from piston.doc import documentation_view

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

FM_Trans_resource = CsrfExemptResource( FM_Trans_Handler )
FM_Bal_resource = CsrfExemptResource( FM_Bal_Handler )

urlpatterns = patterns( '',
    url(r'^fm/trans/user_id/(?P<user_id>.+)/$', FM_Trans_resource),
    url(r'^fm/trans/transaction_id/(?P<transaction_id>.+)/$', FM_Trans_resource),
    url(r'^fm/balance/user_id/(?P<user_id>.+)/$', FM_Bal_resource),
#    url( r'^fm/(?P<expression>.*)$', FM_resource )
)
