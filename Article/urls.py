from django.urls import path

from Article import views
from Article.views import article_listView, detail_view

urlpatterns=[
    path('',views.index),
    path('index_id/<int:id>',views.index_id),
    path('index_template',views.index_template),
    path('list_Article',views.list_Article,name='affichage'),
    path('detail/<int:id>/',views.detail_article,name='D'),
    path('list_view/',article_listView.as_view(),name='afiche_view'),
    path('detail_view/<int:pk>',detail_view.as_view(),name='DD'),
    path('add',views.add_article,name='add'),
    path('add_view',views.Add_Article_View.as_view(),name='add_view'),
    path('delete/<int:id>/',views.Delete,name="Delete"),
    path('deleteV/<int:pk>/', views.Delete_view.as_view(), name="DeleteV"),
    path('update/<int:id>/',views.update_Article,name='Update'),
    path('UpdateV/<int:pk>',views.Update_view.as_view(),name='UpdateV')
    #path('delete/<int:id>/', views.Update, name="Update"),

]