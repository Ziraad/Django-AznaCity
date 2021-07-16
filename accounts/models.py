from django.db import models
from django.contrib.auth.models import User

MALE = 1
FEMALE = 2
GENDER_CHOICES = ((MALE, 'مرد'), (FEMALE, 'زن'))


class Profile(models.Model):
    """
    Represents a user's profile
    """

    class Meta:
        verbose_name = 'نمایه کاربری'
        verbose_name_plural = 'نمایه کاربری'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='حساب کاربری')
    # important fields that are stored in User model:
    #   first_name, last_name, email, date_joined

    mobile = models.CharField('تلفن همراه', max_length=11)

    gender = models.IntegerField('جنسیت', choices=GENDER_CHOICES, null=True, blank=True)

    birth_date = models.DateField('تاریخ تولد', null=True, blank=True)
    address = models.TextField('آدرس', null=True, blank=True)
    profile_image = models.ImageField('تصویر', upload_to='users/profile_images/', null=True, blank=True)

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username

#
# class NewsLetter(models.Model):
#     class Meta:
#         verbose_name = 'خبرنامه'
#         verbose_name_plural = 'خبرنامه'
#
#     email = models.EmailField('ایمیل')
#
#     def __str__(self):
#         return self.email





