from django.db.models import Model, DateTimeField, BooleanField, URLField


class BaseModel(Model):
    created_time = DateTimeField(auto_now_add=True)
    updated_time = DateTimeField(auto_now=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.is_active

    class Meta:
        abstract = True


class SocialMediaUrls(BaseModel):
    facebook = URLField(verbose_name="Facebook")
    twitter = URLField(verbose_name="Twitter")
    instagram = URLField(verbose_name="Instagram")
    linkedin = URLField(verbose_name="LinkedIN")
    youtube = URLField(verbose_name="Youtube")
    whatsapp = URLField(verbose_name="Whatsapp")

    class Meta:
        verbose_name_plural = "Social Media URLS"

    def __str__(self):
        return f"facebook = {self.facebook}, twitter = {self.twitter}, instagram = {self.instagram}, \
         linkedin = {self.linkedin}, youtube = {self.youtube}, whatsapp = {self.whatsapp}"
