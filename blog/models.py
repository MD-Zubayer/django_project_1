from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

# common Field types(Model Field)
# CharField, TextField, IntegerField, FloatField, DecimalField, DateTimeField, DateField, TimeField, BooleanField, EmailField, URLField, FileField, ImageField
class FieldType(models.Model):
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()
    integer_field = models.IntegerField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    float_field = models.FloatField()
    boolean_field = models.BooleanField(default=True)
    created_at_dt = models.DateTimeField(auto_now_add=True)
    created_at_date = models.DateField(auto_now_add=True)
    created_at_time = models.TimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='media/',blank=True, null=True)
    file = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'{self.char_field} - {self.integer_field} - {self.email} - {self.url} - {self.created_at_dt} - {self.created_at_date} - {self.created_at_time} - {self.updated_at  } - {self.boolean_field} - {self.text_field} - {self.float_field} - {self.decimal_field} - {self.image} - {self.file}'

class UserSignUp(models.Model):
    user_name = models.CharField(max_length=100)
    phone_number =  PhoneNumberField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)   
