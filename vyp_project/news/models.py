from django.db import models


class Text(models.Model):
    value = models.TextField()

    def __str__(self):
        return f"{self.value}"


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.ForeignKey('Text', on_delete=models.PROTECT)
    add_date = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='img_news/')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('News', on_delete=models.CASCADE)
