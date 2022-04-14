from django.urls import path
from . import views
urlpatterns = [
    #path('users/', views.UserList.as_view()),
    #path('users/<int:pk>', views.UserDetail.as_view()),
    path('user/<str:uname>', views.getLogin.as_view()),
    path('pr', views.allpurchaseRequest.as_view()),
    path('pr/u/<int:u>', views.userPurchaseRequest.as_view()),
    path('pr/pk/<int:pk>', views.idPurchaseRequest.as_view()),
    #path('')
]