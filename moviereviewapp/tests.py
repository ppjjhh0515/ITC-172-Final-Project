from django.test import TestCase
from .models import Movie, MovieType, Review
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class MovieTypeTest(TestCase):
    def test_string(self):
        type=MovieType(typename='Horror')
        self.assertEqual(str(type), type.typename)

    def test_table(self):
        self.assertEqual(str(MovieType._meta.db_table), 'movietype')

class MovieTest(TestCase):
    def setup(self):
        type = MovieType(typename='Horror')
        movie=Movie(moviename='It', movietype=type, movieprice='9.00')
        return movie
    
    def test_string(self):
        mov = self.setup()
        self.assertEqual(str(mov), mov.moviename)

    def test_type(self):
        mov=self.setup()
        self.assertEqual(str(mov.movietype), 'Horror')
    
    def test_table(self):
        self.assertEqual(str(Movie._meta.db_table), 'movie')

class ReviewTest(TestCase):
   def test_string(self):
       rev=Review(reviewtitle="The best horror")
       self.assertEqual(str(rev), rev.reviewtitle)

   def test_table(self):
       self.assertEqual(str(Review._meta.db_table), 'review')
  
class GetMoviesTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('movies'))
       self.assertEqual(response.status_code, 200)
    
class New_Movie_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=MovieType.objects.create(typename='Horror')
        self.prod = Movie.objects.create(moviename='testmovie1', movietype=self.type, user=self.test_user, movieprice=14.00, movieentrydate='2020-03-05', moviedescription="testmovie for testing")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmovie'))
        self.assertRedirects(response, '/accounts/login/?next=/moviereviewapp/newMovie/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmovie'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moviereviewapp/newmovie.html')