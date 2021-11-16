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
    path('search/see/<int:product_id>/',views.see,name="see"),
    path('search/see/<int:product_id>',views.see,name="see"),
    path('see/payment/<int:product_id>',views.buy,name="buy"),
    path('search/see/payment/<int:product_id>/',views.buy,name="buy"),
    path('search/see/payment/<int:product_id>',views.buy,name="buy"),
    path('payment/verify',views.verifypayment,name="verifypayment"),
    path('payment/verify/',views.verifypayment,name="verifypayment"),
    path('search/',views.search,name="search"),
    path('orders/',views.orders,name="orders"),
    path('orders',views.orders,name="orders"),
    path('logout/',views.logout,name="logout")
] + static(MEDIA_URL,document_root=MEDIA_ROOT)