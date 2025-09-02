from django.db import models
from datetime import date
from django.contrib.auth.models import User 


BOOK_RATE_CHOISES = {
    
    (1, '★☆☆☆☆ - Terrible'),
    (2, '★★☆☆☆ - Poor'),
    (3, '★★★☆☆ - Average'),
    (4, '★★★★☆ - Good'),
    (5, '★★★★★ - Excellent'),
}

GENRE_CHOICES = [
    ('FIC', 'Fiction'),
    ('NF', 'Non-Fiction'),
    ('SCI', 'Science Fiction'),
    ('FAN', 'Fantasy'),
    ('ROM', 'Romance'),
    ('THR', 'Thriller'),
    ('BIO', 'Biography'),
    ('MYS', 'Mystery'),
    ('HIS', 'Historical'),
    ('POE', 'Poetry'),
]


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    publised_date = models.DateField(default=date.today)
    pages = models.PositiveIntegerField()
    rating = models.IntegerField(choices=BOOK_RATE_CHOISES)
    genre = models.CharField(choices=GENRE_CHOICES)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title


# class User(models.Model):
#     user_name = models.CharField()
#     password = models.CharField() 
#     confirm_password = models.CharField()

# from django.contrib.auth.models import User
# class Member(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_name="member",
#     )
#     membership_date = models.DateField(
#         auto_now_add=True
#     )  # only the date it was created, not update instance

#     def __str__(self):
#         r

