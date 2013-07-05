from django.conf.urls import patterns, include
from django.contrib import admin
from mambo.views import index_view, login_view, logout_view, search_view, contact_view, register_view, perfil_view, publica_view


urlpatterns = patterns  ('', 
                           ('^$', index_view),
                           ('^inicio/$',index_view),
                           ('^login/$',login_view), 
                           ('^logout/$',logout_view),
                           ('^search/$',search_view),
                           ('^contact/$',contact_view),
                           ('^register/$',register_view),
                           ('^perfil/$',perfil_view),
                           ('^publica/$',publica_view),
                           ('^admin/', include(admin.site.urls)),
                           )