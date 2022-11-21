from todoapp import views
from django.urls import path

urlpatterns = [
    path('',views.base,name='base'),
    path('add/',views.add,name='add'),
  #  path('detail/',views.detail,name='details')
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.Update,name='update'),
    path('clasb_view/',views.TaskListview.as_view(),name='clasb_view'),
    path('clasb_detail/<int:pk>/',views.TaskDetailview.as_view(),name='clasb_detail'),
    path('clasb_update/<int:pk>/',views.TaskUpdateview.as_view(),name='clasb_update'),
    path('clasb_delete/<int:pk>/',views.TaskDeleteview.as_view(),name='clasb_delete'),
    ]
