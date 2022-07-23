from django.urls import path 
from main import views

urlpatterns = [
    path('',views.Addshow.as_view()),
    path('update/<int:id>/',views.Update.as_view(),name='update'),
    path('delete/<int:id>/',views.delete1.as_view(),name='delete'),

]
