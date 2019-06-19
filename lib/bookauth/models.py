from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    published_at = models.DateField(max_length=50)
    author_det = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.name
