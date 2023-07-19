from django.urls import path
from . import views
from boards import views




urlpatterns = [

    path("",views.home,name ='index'),
    #path('about/',views.about,name='about'),
    path('boards/<int:board_id>/',views.board_topics,name = 'board_topics'),
    path('boards/<int:board_id>/new/',views.new_topic, name ='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>', views.topic_posts , name ='topic_posts' ),
    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),


    
]
