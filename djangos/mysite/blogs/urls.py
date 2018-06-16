from django.views.generic import ListView, DetailView
from django.conf.urls import url, include
from blogs.models import Post
import blogs.views

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],
        template_name="blogs/blogs.html")),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model = Post,
        template_name="blogs/post.html")),
    url(r'timeseries', blogs.views.TimeSeriesAnalysis, name='TimeSeriesAnalysis'),
    url(r'python-map-apply', blogs.views.AdvancedTopicsMapApply, name='AdvancedTopicsMapApply'),
    url(r'biostats1', blogs.views.BioStats1, name='biostats1'),
    url(r'biostats2', blogs.views.BioStats2, name='biostats2'),
    url(r'biostats3', blogs.views.BioStats3, name='biostats3'),
    url(r'sas1', blogs.views.ReadingSaSDataSets, name='sas1'),
    url(r'sas2', blogs.views.ControllingInputOutputSAS, name='sas2'),
    url(r'sas3', blogs.views.AppendConcatenate, name='sas3'),
    url(r'sas4', blogs.views.AccumulateSAS, name='sas4'),
    url(r'machinelearning1', blogs.views.Classification1, name='machinelearning1'),
]
