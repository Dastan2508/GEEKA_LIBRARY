from django.db import models


class Books(models.Model):
    GENRE_CHOICE = (
        ('Художественный', 'Художественный'),
        ('Детектив', 'Детектив'),
        ('Фантастика', 'Фантастика')
    )

    image = models.ImageField(upload_to='book/',verbose_name='Обложка книги', null=True )
    title = models.CharField(max_length=100,verbose_name='Укажите описание книги')
    description = models.TextField(verbose_name='Укажите описание к книге')
    price = models.FloatField(verbose_name='Укажите цену')
    start_book = models.DateField(verbose_name='Укажите дату выхода',null=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, verbose_name='Укажите жанр книги')
    mail = models.CharField(max_length=100, verbose_name='Укажите почту автора книги')
    name = models.CharField(max_length=100,verbose_name='Имя автора')
    audio = models.URLField(verbose_name='Укажите ссылку на аудио данной книги с youtube', null=True)

    class Meta:
        verbose_name ='книга'
        verbose_name_plural = 'книги'



    def __str__(self):
        return f'{self.title}-{self.price}$'
