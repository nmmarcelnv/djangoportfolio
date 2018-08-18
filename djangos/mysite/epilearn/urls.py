from django.conf.urls import url
from epilearn.views import EpilearnView, SIRmodelView

urlpatterns = [
    url(r'^$', EpilearnView.as_view(), name='epilearn'),
    url(r'^sirmodel$', SIRmodelView.as_view(), name='sirmodel'),
]
