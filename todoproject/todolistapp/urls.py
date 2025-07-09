from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name=""),
	path('update/<str:temp>/',views.updatetask,name="update"),
	path('delete/<str:temp>/',views.deletetask,name="delete"),
]
