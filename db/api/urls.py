from django.urls import path
from . import views
urlpatterns = [
    #path('users/', views.UserList.as_view()),
    #path('users/<int:pk>', views.UserDetail.as_view()),
    path('user/<str:uname>', views.getLogin.as_view()),
    path('pr', views.allpurchaseRequest.as_view()),
    path('pr/u/<int:u>', views.userPurchaseRequest.as_view()),
    path('pr/pk/<int:pk>', views.idPurchaseRequest.as_view()),
    path('it', views.allItems.as_view()),
    path('it/pk/<int:pk>', views.updateItem.as_view()),
    path('iv', views.allInvoices.as_view()),
    path('iv/pk/<int:pk>', views.updateInvoice.as_view()),
]