from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
# Create your views here.

class MovieAPIListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers 

class MovieAPICreatView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

class MovieAPIUpdateView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers 

class MovieAPIDestroyView(DestroyAPIView):
    queryset = Movie.objects.all()


class MovieAPIDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers 

class MovieAPIDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers 



class ActorAPIListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers 

class ActorAPICreatView(CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers 

class ActorAPIUpdateView(RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers 

class ActorAPIDestroyView(DestroyAPIView):
    queryset = Actor.objects.all()


class ActorAPIDetailView(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers 

class ActorAPIDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers 



class GenresAPIListView(ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers 

class GenresAPICreatView(CreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers 

class GenresAPIUpdateView(RetrieveUpdateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers 

class GenresAPIDestroyView(DestroyAPIView):
    queryset = Genres.objects.all()


class GenresAPIDetailView(RetrieveAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers 

class GenresAPIDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers 


class ReviewerAPIListView(ListAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializers 

class ReviewerAPICreatView(CreateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializers 

class ReviewerAPIUpdateView(RetrieveUpdateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializers 

class ReviewerAPIDestroyView(DestroyAPIView):
    queryset = Reviewer.objects.all()


class ReviewerAPIDetailView(RetrieveAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializers 

class ReviewerAPIDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializers 



class DirectorAPIListView(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers 

class DirectorAPICreatView(CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers 

class DirectorAPIUpdateView(RetrieveUpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers 

class DirectorAPIDestroyView(DestroyAPIView):
    queryset = Director.objects.all()


class DirectorAPIDetailView(RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers 

class DirectorAPIDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers 



class MovieCastAPIListView(ListAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializers 

class MovieCastAPICreatView(CreateAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializers 

class MovieCastAPIUpdateView(RetrieveUpdateAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializers 

class MovieCastAPIDestroyView(DestroyAPIView):
    queryset = MovieCast.objects.all()


class MovieCastAPIDetailView(RetrieveAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializers 

class MovieCastAPIDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializers 



class RatingAPIListView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers 

class RatingAPICreatView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers 

class RatingAPIUpdateView(RetrieveUpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers 

class RatingAPIDestroyView(DestroyAPIView):
    queryset = Rating.objects.all()


class RatingAPIDetailView(RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers 

class RatingAPIDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers 
