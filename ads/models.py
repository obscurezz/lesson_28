from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    id = models.AutoField(primary_key=True)

    def __str__(self):
        if hasattr(self, "name"):
            return self.name
        if hasattr(self, "username"):
            return self.username

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Location(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(BaseModel):
    ROLES = [
        ('admin', 'admin'),
        ('member', 'member'),
        ('moderator', 'moderator'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=15, choices=ROLES, default='member')
    age = models.PositiveIntegerField(default=18)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



class Ad(BaseModel):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=4000)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='logos/', default='logos/logo.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    @property
    def get_image_url(self):
        return self.image.url

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-price']
