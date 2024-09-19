from django.db import models

class NewsArticle(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=22, choices=[
        ('entertainment', 'Entertainment'),
        ('sports', 'Sports'),
        ('national', 'National'),
        ('international', 'International'),
        ('science_and_tech', 'Science & Tech'),
        ('business_and_economics', 'Business & Economics')
    ])
    published_date = models.DateTimeField()
    image = models.FileField(upload_to='news_articles/images/', blank=True, null=True)

    def __str__(self):
        return self.title