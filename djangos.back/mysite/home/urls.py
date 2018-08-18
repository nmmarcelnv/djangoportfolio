from django.conf.urls import url
from home.views import HomeView, TimeSeriesAnalysis

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^timeseries/', TimeSeriesAnalysis, name='TimeSeriesAnalysis'),
]
