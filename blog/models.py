from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    # this line defines our model(It is an object.)
    # "class" is a special keyword that indicates that we are defining an object
    # "Post" is the name of our model. Always start a class name with an uppercase letter.
    # "models.Model" means that the Post is a Django Model, so Django knows that it should be saved in the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
# ? ? ? what this method doesn't have a name?
    def __str__(self):
        # in this scenario, when we call "__str__()" we will get a text(string) with a Post tile.
        return self.title
