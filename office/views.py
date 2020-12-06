from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import County, HeadOffice, RegionalOffice, FieldOffice


class HomePageView(TemplateView):
    template_name = 'index.html'


def HeadOfficeData(request):
    offices = serialize('geojson', HeadOffice.objects.all())
    return HttpResponse(offices, content_type='json')


def RegionalOfficeData(request):
    offices = serialize('geojson', RegionalOffice.objects.all())
    return HttpResponse(offices, content_type='json')


def FieldOfficeData(request):
    offices = serialize('geojson', FieldOffice.objects.all())
    return HttpResponse(offices, content_type='json')


def CountyData(request):
    counties = serialize('geojson', County.objects.all())
    return HttpResponse(counties, content_type='json')
