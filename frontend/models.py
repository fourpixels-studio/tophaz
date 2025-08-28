from django.db import models
from django_resized import ResizedImageField
from django.templatetags.static import static


class Homepage(models.Model):
    image_1 = models.FileField(upload_to="homepage/", blank=True, null=True)
    image_2 = models.FileField(upload_to="homepage/", blank=True, null=True)
    image_3 = models.FileField(upload_to="homepage/", blank=True, null=True)
    image_4 = models.FileField(upload_to="homepage/", blank=True, null=True)
    image_5 = models.FileField(upload_to="homepage/", blank=True, null=True)

    about_title = models.CharField(max_length=80, blank=True, null=True)
    about_paragraph = models.TextField(blank=True, null=True)

    mixes_cover = models.FileField(
        upload_to="homepage/", blank=True, null=True)
    shows_cover = models.FileField(
        upload_to="homepage/", blank=True, null=True)
    shop_cover = models.FileField(upload_to="homepage/", blank=True, null=True)

    seo_description = models.TextField(blank=True, null=True)
    seo_keywords = models.TextField(blank=True, null=True)
    seo_title = models.TextField(blank=True, null=True)
    seo_thumbnail = models.FileField(
        upload_to="homepage/", blank=True, null=True, help_text="Thumbnail dimensions: 1200px x 633px")
    resized_meta_thumbnail = ResizedImageField(size=[1200, 633], crop=[
        'middle', 'center'], quality=75, upload_to='thumbnails/', blank=True, null=True)

    @property
    def get_meta_thumbnail(self):
        if self.resized_meta_thumbnail:
            return self.resized_meta_thumbnail.url
        return static('tophaz_meta_thumbnail.jpg')

    def __str__(self):
        return str("Homepage")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.seo_thumbnail and (not self.resized_meta_thumbnail or self.resized_meta_thumbnail.name != f"{self.seo_thumbnail.name}"):
            self.seo_thumbnail.save(
                f"{self.seo_thumbnail.name}", self.seo_thumbnail, save=False)
            super().save(update_fields=['resized_meta_thumbnail'])


class BioPage(models.Model):
    hero_image = models.FileField(upload_to="bio/", blank=True, null=True)
    main_title = models.CharField(max_length=80, blank=True, null=True)
    paragraph = models.TextField(blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    seo_keywords = models.TextField(blank=True, null=True)
    seo_title = models.TextField(blank=True, null=True)
    seo_thumbnail = models.FileField(
        upload_to="bio/", blank=True, null=True, help_text="Thumbnail dimensions: 1200px x 633px")
    resized_meta_thumbnail = ResizedImageField(size=[1200, 633], crop=[
        'middle', 'center'], quality=75, upload_to='thumbnails/', blank=True, null=True)

    @property
    def get_meta_thumbnail(self):
        if self.resized_meta_thumbnail:
            return self.resized_meta_thumbnail.url
        return static('tophaz_meta_thumbnail.jpg')

    def __str__(self):
        return str("Bio Page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.seo_thumbnail and (not self.resized_meta_thumbnail or self.resized_meta_thumbnail.name != f"{self.seo_thumbnail.name}"):
            self.seo_thumbnail.save(
                f"{self.seo_thumbnail.name}", self.seo_thumbnail, save=False)
            super().save(update_fields=['resized_meta_thumbnail'])


class Bookings(models.Model):
    name = models.CharField(max_length=180, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    date = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=180, blank=True, null=True)
    city = models.CharField(max_length=180, blank=True, null=True)
    website = models.CharField(max_length=180, blank=True, null=True)
    instagram = models.CharField(max_length=180, blank=True, null=True)
    facebook = models.CharField(max_length=180, blank=True, null=True)
    twitter = models.CharField(max_length=180, blank=True, null=True)
    budget = models.CharField(max_length=8, blank=True, null=True)
    other_acts = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    submited_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
