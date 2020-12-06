from django.urls import path
from .views import HomePageView, CountyData, HeadOfficeData, RegionalOfficeData, FieldOfficeData

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('counties/', CountyData, name='counties'),
    path('head_offices/', HeadOfficeData, name='head_office'),
    path('field_offices/', FieldOfficeData, name='field_office'),
    path('regional_offices/', RegionalOfficeData, name='regional_office'),
]
