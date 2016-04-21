from django.conf.urls import include, url
from live_system_products import views

urlpatterns = [
    url(r'^$', views.LspResults.as_view(), name='home'),
    url(r'^results/$', views.LspResults.as_view(), name='lsp_results'),
    url(r'^qa_status/$', views.QAStatus.as_view(), name='qa_status'),
    url(r'^deploy_status/$', views.DeployStatus.as_view(), name='deploy_status'),
    url(r'^deploy_receiver/$', views.DeployReceiver.as_view(), name="deploy_receiver")
]
