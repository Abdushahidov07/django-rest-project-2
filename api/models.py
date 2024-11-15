from django.db import models

# Create your models here.

class Movie(models.Model):
    mov_title = models.CharField(max_length=50)
    mov_year = models.IntegerField()
    mov_time = models.IntegerField()
    mov_lang = models.CharField(max_length=50)
    mov_dl_rel = models.DateField(auto_now=False, auto_now_add=False)
    mov_rel_country = models.CharField(max_length=50)
    def __str__(self):
        return self.mov_title
    

class Actor(models.Model):
    act_fname = models.CharField(max_length=50)
    act_fname = models.CharField(max_length=50)
    act_gemder = models.CharField(max_length=1)
    def __str__(self):
        return self.act_fname

class MovieCast(models.Model):
    act_id = models.ForeignKey(Actor,on_delete=models.CASCADE)
    mov_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    def __str__(self):
        return self.role
    

class Genres(models.Model):
    mov_id = models.ManyToManyField(Movie, verbose_name=("movie"))
    gen_title = models.CharField( max_length=20)
    def __str__(self):
        return self.gen_title
    
class Reviewer(models.Model):
    rev_name = models.CharField(max_length=30)
    def __str__(self):
        return self.rev_name
    

class Rating(models.Model):
    mov_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rev_id = models.ForeignKey(Reviewer,on_delete=models.CASCADE)
    rev_starts = models.IntegerField()
    num_o_ratings = models.IntegerField()
    def __str__(self):
        return self.rev_starts
    

class Director(models.Model):
    mov_id = models.ManyToManyField(Movie, verbose_name=("Director movie"))
    dir_fname = models.CharField(max_length=50)
    dir_lname = models.CharField(max_length=50)
    def __str__(self):
        return self.dir_fname    
