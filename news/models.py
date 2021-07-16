from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User
from city.models import IpClass
from ckeditor_uploader.fields import RichTextUploadingField

from django.urls import reverse


class Category(models.Model):
    name = models.CharField('نام', max_length=40)
    slug = models.SlugField('اسلاگ',
                            help_text='نام دسته بندی را به انگلیسی ترجمه کنید و در این قسمت تایپ کنید!خط فاصله ها را '
                                      'با "-" پرکنید!',
                            max_length=100, allow_unicode=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children',
                               verbose_name='سردسته')
    image = models.ImageField('تصویر', upload_to='CategoryImages/', blank=True)
    description = models.TextField('توضیحات', null=True, blank=True)

    def get_absolute_url(self):
        if self.parent == None:
            return reverse('cryptocur:parent_cat_page', args=[self.slug])
        else:
            return reverse('cryptocur:sub_cat_page', args=[self.parent.slug, self.slug])

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])


class News(models.Model):
    class Meta:
        verbose_name = 'اخبار'
        verbose_name_plural = "اخبار"

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='نویسنده')
    title = models.CharField('عنوان', max_length=200)
    slug = models.SlugField('اسلاگ',
                            help_text='عنوان را به انگلیسی ترجمه کنید و در این قسمت تایپ کنید!خط فاصله ها را با "-" '
                                      'پرکنید!',
                            max_length=200,
                            allow_unicode=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی")
    image = models.ImageField('تصویر', upload_to='newsImages/', null=False, blank=True)
    text = RichTextUploadingField('متن خبر', null=True)
    study_time = models.IntegerField('زمان مطالعه')
    selected_editor = models.BooleanField('منتخب سردبیر', default=False, null=True)
    views = models.ManyToManyField(IpClass, related_name='post_views', verbose_name='نمایش', blank=True)
    pub_date = models.DateTimeField('تاریخ انتشار', auto_now_add=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author) + str(self.pub_date)

    def get_absolute_url(self):
        return reverse('news:news_detail_page', args=[self.category.parent.slug, self.category.slug, self.slug])

    def total_views(self):
        return self.views.count()
