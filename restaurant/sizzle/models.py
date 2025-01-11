from django.db import models

# Create your models here.
class ItemList(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name

class Items(models.Model):
    item_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    category = models.ForeignKey(ItemList, related_name='name', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.item_name


class AboutUs(models.Model):
    description = models.TextField(blank=False)

class Feedback(models.Model):
    user_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='items/', blank=True)
    def __str__(self):
        return self.user_name


class BookTable(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    email = models.EmailField()
    total_person = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name

