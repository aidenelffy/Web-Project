from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from knox import views as knox_views
from .views.views_cbv import PostListAPIView, PostDetailAPIView, \
    Post1, Post2, Post3, Post4, Post5, RegisterAPI, LoginAPI, OrderAPIView
from .views.views_fbv import product_detail, product_list, product_furniture, furniture_list, furniture_detail, \
    orders_list

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('post/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),

    path('post/post1', Post1.as_view()),
    path('post/post2', Post2.as_view()),
    path('post/post3', Post3.as_view()),
    path('post/post4', Post4.as_view()),
    path('post/post5', Post5.as_view()),


    path('product/', product_list),
    path('product/<int:product_id>/', product_detail),


    path('furniture/', furniture_list),
    path('furniture/<int:furniture_id>/', furniture_detail),
    path('product/<int:product_id>/furniture/', product_furniture),

    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),

    path('order/', orders_list),
    path('order/<int:pk>', OrderAPIView.as_view()),
]