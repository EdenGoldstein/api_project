
from rest_framework import routers
from books import views
from django.urls import path, include
# from .views import UserRegistrationView, UserLoginView

app_name = "books"


urlpatterns = [
    
    path('author/', views.AuthorListCreate.as_view()),
    path('author/<int:pk>', views.AuthorDetail.as_view()),
   
]

router = routers.DefaultRouter()

router.register('books', views.BookViewSet)
urlpatterns += router.urls
