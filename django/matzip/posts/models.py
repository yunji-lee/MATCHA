from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill    # Resizeing 하는 이유는 사용자에게 파일을,# 그대로 제공하지말고 썸네일 식으로 제공
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Post(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(blank=True)  ## blank 는 이미지를 안넣고 migrate 가 가능
    image = ProcessedImageField(
        upload_to='posts/images',                 ## 올리는 위치 설정
        processors=[ResizeToFill(600, 600)],       ## 사이즈를 정한다.
        format='JPEG',
        options={'quality': 90}
    )


class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Matzip_list(models.Model):
    store_name = models.TextField(blank=True)
    category = models.TextField(blank=True)
    review = models.IntegerField(blank=True)
    tv = models.TextField(blank=True)
    biztel = models.TextField(blank=True)
    address = models.TextField(blank=True)
    Menu = models.TextField(blank=True)
    homepage = models.TextField(blank=True)
    facebook = models.TextField(blank=True)
    instagram = models.TextField(blank=True)
    blog = models.TextField(blank=True)
    web_site = models.TextField(blank=True)
    convenience = models.TextField(blank=True)
    desc = models.TextField(blank=True)
    age10 = models.CharField(max_length=50, blank=True)
    age20 = models.CharField(max_length=50, blank=True)
    age30 = models.CharField(max_length=50, blank=True)
    age40 = models.CharField(max_length=50, blank=True)
    age50 = models.CharField(max_length=50, blank=True)
    age60 = models.CharField(max_length=50, blank=True)
    Female = models.CharField(max_length=50, blank=True)
    male = models.CharField(max_length=50, blank=True)
    images_url_preprocess = models.URLField(blank=True)
    new_urls = models.URLField(blank=True)

    class Meta:
        ordering = ['-id']


class Star(models.Model):
    rate = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    matzip = models.ForeignKey(Matzip_list, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        import csv
        file = open('stars.csv', 'a+', encoding='utf-8', newline='')
        writer = csv.writer(file)
        writer.writerow([self.user_id, self.matzip_id, self.rate])
        file.close()