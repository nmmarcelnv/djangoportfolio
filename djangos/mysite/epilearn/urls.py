from django.conf.urls import url
from epilearn.views import EpilearnView

urlpatterns = [
    url(r'^$', EpilearnView.as_view(), name='epilearn'),
]
