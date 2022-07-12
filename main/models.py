from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


# from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify
# from ckeditor.fields import RichTextField

'''Responsable for the user object creation and the fields needed for that'''
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('the given username is not valid')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser, 
                            date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields)

    def create_staffuser(self, username, email, password, **extra_fields):
        user =  self._create_user(username, email, password, is_active=True, is_staff=True, is_superuser=False, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user =  self._create_user(username, email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)
        user.save(using=self._db)
        return user

''' User model or fields that we need to add '''
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now())
    profile_image = models.ImageField(blank=True, null=True, upload_to="avatar")
    birth_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    about_me = models.TextField(max_length=500, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
# class Skill(models.Model):
#     class Meta:
#         verbose_name_plural = 'Skills'
#         verbose_name = 'Skill'
    
#     name = models.CharField(max_lenght=20, blank=True, null=True)
#     score = models.IntegerField(default=80, blank=True, null=True)
#     image = models.FileField(blank=True, null=True, upload_to="skills")
#     is_key_skill = models.BooleanField(default=False)

#     def _str_(self):
#         return self.name


# class UserProfile(models.Model):
#     class Meta:
#         verbose_name_plural = 'User Pofiles'
#         verbose_name = 'User Profile'

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
#     title = models.CharField(max_length=200, blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     skills = models.ManytoManyField(Skill, blank=True)
#     cv = models.FileField(blank=True, null=True, upload_to="cv")

#     def _str_(self):
#         return f'{self.user.first_name} {self.user.last_name}'


# class ContactProfile(models.Model):
#     class Meta:
#         verbose_name_plural = 'Contact Pofiles'
#         verbose_name = 'Contact Profile'
#         ordering = ["timestamp"]

#     timestamp = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(verbose_name="Name", max_length=100)
#     email = models.EmailField(verbose_name="Email")
#     message = models.TextField(verbose_name="Message")

#     def _str_(self):
#         return f'{self.name}'

# class Testimonial(models.Model):
#     class Meta:
#         verbose_name_plural = 'Testimonials'
#         verbose_name = 'Testimonial'
#         ordering = ["name"]

#     thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
#     name = models.CharField(max_length=200, blank=True, null=True)
#     role = models.CharField(max_length=200, blank=True, null=True)
#     quote = models.CharField(max_length=200, blank=True, null=True)
#     is_active = models.BooleanField(default=True)

#     def _str_(self):
#         return self.name

# class Media(models.Model):
#     class Meta:
#         verbose_name_plural = 'Media Files'
#         verbose_name = 'Media File'
#         ordering = ["name"]

#     image  = models.ImageField(blank=True, null=True, upload_to="media")
#     url = models.URLField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     is_image = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if self.url:
#             self.is_image = False
#         super(Media, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name


# class Portafolio(model.Models):
#     class Meta:
#         verbose_name_plural = 'Portafolios'
#         verbose_name = 'Portafolio'
#         ordering = ["name"]

#     date = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     body = RichTextField(blank=True, null=True)
#     image = models.ImageField(blank=True, null=True, upload_to="portafolio")
#     slug = models.SlugField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.name)
#         super(Portafolio, self).save(*args, **kwargs)

#     def _str_(self):
#         return self.name

#     def get_absolute_url(self):
#         return f"/portafolio/{self.slug}"

# class Blog(models.Model):

#     class Meta:
#         verbose_name_plural = 'Blog Profiles'
#         verbose_name = 'Blog'
#         ordering = ["timestamp"]

#     timestamp = models.DateTimeField(auto_now_add=True)
#     author = models.CharField(max_length=200, blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     body = RichTextField(blank=True, null=True)
#     slug = models.SlugField(null=True, blank=True)
#     image = models.ImageField(blank=True, null=True, upload_to="blog")
#     is_active = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.name)
#         super(Blog, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return f"/blog/{self.slug}"


# class Certificate(models.Model):

#     class Meta:
#         verbose_name_plural = 'Certificates'
#         verbose_name = 'Certificate'

#     date = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     title = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

