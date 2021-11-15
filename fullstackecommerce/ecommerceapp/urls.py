from django.urls import path
from . import views
from fullstackecommerce.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('products/',views.products,name="products"),
    path('register/',views.register,name="register"),
    path('register',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('login',views.login,name="login"),
    path('see/<int:product_id>',views.see,name="see"),
    path('payment/<int:product_id>',views.payment,name="payment"),
    path('logout/',views.logout,name="logout")
] + static(MEDIA_URL,document_root=MEDIA_ROOT)