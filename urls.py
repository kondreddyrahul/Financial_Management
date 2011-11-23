from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cooperative_Bank.views.home', name='home'),
    # url(r'^cooperative_Bank/', include('cooperative_Bank.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^cooperative_Bank/admin/', include(admin.site.urls)),
    url(r'^api/', include('cooperative_Bank.api.urls')),
    url(r'^cooperative_Bank/$', 'cooperative_Bank.financial_management.views.login_page'),
    url(r'^cooperative_Bank/fm/user$','cooperative_Bank.financial_management.views.account_detail'),
    url(r'^cooperative_Bank/fm/MF$','cooperative_Bank.financial_management.views.mf_detail'),
    url(r'^cooperative_Bank/fm/FO$','cooperative_Bank.financial_management.views.fo_detail'),
    url(r'^cooperative_Bank/fm/IPO$','cooperative_Bank.financial_management.views.ipo_detail'),
    url(r'^cooperative_Bank/fm/Thank$','cooperative_Bank.financial_management.views.thank_detail'),
    url(r'^cooperative_Bank/fm/Thank1$','cooperative_Bank.financial_management.views.thank1_detail'),
    url(r'^cooperative_Bank/fm/Thank2$','cooperative_Bank.financial_management.views.thank2_detail'),
    url(r'^cooperative_Bank/fm/Trans$','cooperative_Bank.financial_management.views.trans_detail'),
    #url(r'^Bank/fm/mf$','cooperative_Bank.financial_management.views.mf'),

)
