from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostsDetail, NewsFilter, NewsCreate, NewsUpdate, NewsDelete


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostsDetail.as_view()),
   path('search', NewsFilter.as_view()),
   path('create', NewsCreate.as_view()),
   path('<int:pk>/edit/', NewsUpdate.as_view()),
   path('<int:pk>/delete/', NewsDelete.as_view()),
]
