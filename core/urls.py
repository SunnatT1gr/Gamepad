from django.urls import path
from .views import homeview, ContactView, AboutView, ProductView, RemotView, VideoView

app_name = 'core'
urlpatterns = [
    path('', homeview, name="home_page"),
    path('contact/', ContactView.as_view(), name="contact_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('product/', ProductView.as_view(), name="product_page"),
    path('remot/', RemotView.as_view(), name="remot_page"),
    path('video/', VideoView.as_view(), name="video_page")
]