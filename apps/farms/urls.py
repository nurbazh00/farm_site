from django.urls import path

from apps.farms.views import AboutUsView, CompaniesView, LandingView, \
    CompanyDetailView, SuccessView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('about_us', AboutUsView.as_view(), name='about_us'),
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('company/<int:pk>', CompanyDetailView.as_view(), name='company'),
    path('success', SuccessView.as_view(), name='success'),
]
