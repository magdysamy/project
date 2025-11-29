from django.urls import path    
from . import views

urlpatterns = [
    path('',views.index ,name='index' ),
    path('create-book', views.Bookgreate.as_view(), name='create_book'),
    path('detail/<int:pk>', views.Bookdetail.as_view(), name='detail'),
    path('accounts/register', views.register.as_view (), name='register'),
]