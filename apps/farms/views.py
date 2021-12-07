import json

from django.http import JsonResponse
from django.views.generic import TemplateView, DetailView, ListView

from apps.farms.models import Company, About_us, Success_story, Companies, \
    Product, Contact


class LandingView(TemplateView):
    template_name = 'pages/Landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.all()
        context['about_us'] = About_us.objects.all()
        context['contact'] = Contact.objects.all()

        return context


class CompaniesView(ListView):
    model = Company
    template_name = 'pages/Companies.html'

    def get_context_data(self, **kwargs):
        context = super(CompaniesView, self).get_context_data(**kwargs)
        context['companies'] = Companies.objects.all()

        return context


class CompanyDetailView(DetailView):
    template_name = 'pages/company.html'
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        company = context.get('company')
        context['product'] = Product.objects.filter(
            company__id=company.id
        )

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())

        company = Company.objects.filter(id=data.get('company_id')).first()

        if company is None:
            return JsonResponse({'detail': 'error'}, status=404)


class SuccessView(TemplateView):
    template_name = 'pages/success.html'

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['success'] = Success_story.objects.all()

        return context


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['about_us'] = About_us.objects.all()

        return context