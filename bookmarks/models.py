from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# python manage.py syncdb ==> python manage.py migrate 으로 변경됨
# migrate 가 안되면 makemigrations 실행 후 migrate 실행
class Link(models.Model):
    url = models.URLField(unique=True)

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)