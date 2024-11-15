from django.urls import path
from .views import *
urlpatterns = [
    path('', MovieAPIListView.as_view(), name='home'),
    path("movie/create", MovieAPICreatView.as_view(), name="moviecreate"),
    path("movie/<int:pk>/update", MovieAPIUpdateView.as_view(), name="updatemovie"),
    path("movie/<int:pk>/delete", MovieAPIDestroyView.as_view(), name="deletemovie"),
    path('movie/<int:pk>', MovieAPIDetailView.as_view(), name='detailmovie'),



    path('actor', ActorAPIListView.as_view(), name='actor'),
    path("actor/create", ActorAPICreatView.as_view(), name="Actorcreate"),
    path("actor/<int:pk>/update", ActorAPIUpdateView.as_view(), name="updateActor"),
    path("actor/<int:pk>/delete", ActorAPIDestroyView.as_view(), name="deleteActor"),
    path('actor/<int:pk>', ActorAPIDetailView.as_view(), name='detailActor'),

    path('genres', GenresAPIListView.as_view(), name='genres'),
    path("genres/create", GenresAPICreatView.as_view(), name="Genrescreate"),
    path("genres/<int:pk>/update", GenresAPIUpdateView.as_view(), name="updateGenres"),
    path("genres/<int:pk>/delete", GenresAPIDestroyView.as_view(), name="deleteGenres"),
    path('genres/<int:pk>', GenresAPIDetailView.as_view(), name='detailGenres'),


    path('reviewer', ReviewerAPIListView.as_view(), name='reviewer'),
    path("reviewer/create", ReviewerAPICreatView.as_view(), name="Reviewercreate"),
    path("reviewer/<int:pk>/update", ReviewerAPIUpdateView.as_view(), name="updateReviewer"),
    path("reviewer/<int:pk>/delete", ReviewerAPIDestroyView.as_view(), name="deleteReviewer"),
    path('reviewer/<int:pk>', ReviewerAPIDetailView.as_view(), name='detailReviewer'),


    path('director', DirectorAPIListView.as_view(), name='director'),
    path("director/create", DirectorAPICreatView.as_view(), name="Directorcreate"),
    path("director/<int:pk>/update", DirectorAPIUpdateView.as_view(), name="updateDirector"),
    path("director/<int:pk>/delete", DirectorAPIDestroyView.as_view(), name="deleteDirector"),
    path('director/<int:pk>', DirectorAPIDetailView.as_view(), name='detailDirector'),
]
