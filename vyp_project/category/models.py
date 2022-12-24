from django.db import models


class Date(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return f"{self.value}"


class ScreenSize(models.Model):
    value = models.DecimalField(max_digits=2, decimal_places=1, help_text='Дюймы')

    def __str__(self):
        return f"{self.value}"


class Ram(models.Model):
    value = models.IntegerField(help_text='ГБ')

    def __str__(self):
        return f"{self.value}"


class Memory(models.Model):
    value = models.IntegerField(help_text='ГБ')

    def __str__(self):
        return f"{self.value}"


class Phone(models.Model):
    name = models.CharField(max_length=50)
    date = models.ForeignKey('Date', on_delete=models.PROTECT)
    screen_size = models.ForeignKey('ScreenSize', on_delete=models.PROTECT)
    ram = models.ForeignKey('Ram', on_delete=models.PROTECT)
    memory = models.ForeignKey('Memory', on_delete=models.PROTECT)
    add_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img_category/')

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Phone', on_delete=models.CASCADE)
