from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request, 'index.html')

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ProductView(TemplateView):
    template_name = 'product.html'
    
class RemotView(TemplateView):
    template_name = 'remot.html'

class VideoView(TemplateView):
    template_name = 'video.html'
