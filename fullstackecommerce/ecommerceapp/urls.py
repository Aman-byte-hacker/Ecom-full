from django.urls import path
from . import views
from fullstackecommerce.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
] + static(MEDIA_URL,document_root=MEDIA_ROOT)