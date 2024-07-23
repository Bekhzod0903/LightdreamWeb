from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Musics(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    music = models.FileField(upload_to='music')  # Tekshiring: Bu maydon modelda mavjud bo'lishi kerak

    def save(self, *args, **kwargs):
        if not self.genre:
            default_category, created = Category.objects.get_or_create(name="Boshqalar")
            self.genre = default_category
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video = models.FileField(upload_to='news_videos/', blank=True, null=True)

    def __str__(self):
        return self.title
