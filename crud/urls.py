from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('myProducts', views.myProducts, name='myProducts'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

]