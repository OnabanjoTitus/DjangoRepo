from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'Home.html'


class AboutPageView(TemplateView):
    template_name = 'About.html'
