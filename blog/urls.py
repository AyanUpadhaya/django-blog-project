
from django.urls import path
from .views import index,detail_view
urlpatterns = [
    path('', index,name="home"),
    path('/post/<int:pk>',detail_view,name='detail')
]