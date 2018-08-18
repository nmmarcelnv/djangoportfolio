from django.conf.urls import url
from disease.views import DiseaseView

urlpatterns = [
    url(r'^$', DiseaseView.as_view(), name='disease'),
]
