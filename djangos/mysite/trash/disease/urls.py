from django.conf.urls import url
from diseases.views import DiseaseView

urlpatterns = [
    url(r'^$', DiseaseView.as_view(), name='disease'),
]
