from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(0)
    views = models.IntegerField(0)

    class Meta:
            verbose_name_plural = 'Categories'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category,
    on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    class Meta:
            verbose_name_plural = 'Pages'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.title
