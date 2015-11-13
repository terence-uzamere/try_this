from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

VISIBILITY_CHOICES = (
(0, 'Night Life'),
(1, 'Restaurants'),
(2, 'Movies/TV Shows'),
(3, 'Recipes'),
(4, 'Food'),
(5, 'Lifestyle'),
)


# Create your models here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Suggestion(models.Model):
  title = models.CharField(max_length=300)
  caption = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
  category = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("suggestion_detail", args=[self.id])

class Comments(models.Model):
  suggestion = models.ForeignKey(Suggestion)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

  def __unicode__(self):
    return self.text

class Vote(models.Model):
  user = models.ForeignKey(User)
  suggestion = models.ForeignKey(Suggestion)

  def __unicode__(self):
    return "%s upvoted" % (self.user.username)




