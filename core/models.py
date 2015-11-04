from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse 

# Create your models here.
class Try(models.Model):
  category = models.CharField(max_length=300)
  caption = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("try_detail", args=[self.id])