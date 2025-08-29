from django.db import models


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

class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField
    pages = models.PositiveIntegerField
    rating = models.IntegerField(choices=BOOK_RATE_CHOISES)
    genre = models.CharField(choices=GENRE_CHOICES)
    
    def __str__(self):
        return self.title
