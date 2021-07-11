from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

PLACE_CATEGORY = (
    ('H', 'تاریخی'),
    ('M', 'مذهبی'),
    ('T', 'گردشگری'),
    ('R', 'روستا'),
    ('K', 'کارخانجات'),
)

SOGHAT_CATEGORY = (
    ('F', 'خوراکی'),
    ('D', 'صنایع دستی'),
)

HOTEL_RES_CATEGORY = (
    ('H', 'هتل'),
    ('R', 'رستوران'),
)


class IpClass(models.Model):
    ip = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ip


class Category(models.Model):
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'

    name = models.CharField('نام', max_length=40)
    slug = models.SlugField('اسلاگ', max_length=40, allow_unicode=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children',
                               verbose_name='سردسته')
    # description = models.TextField('توضیحات', null=True, blank=True)
    image = models.ImageField(upload_to='categorys', verbose_name='عکس', null=True, blank=True)
    icon = models.ImageField(upload_to='categorys/icon', verbose_name='آیکون', null=True, blank=True)
    icon_name = models.CharField('نام آیکون', max_length=50, null=True, blank=True)
    body = RichTextUploadingField('توضیحات')

    def get_absolute_url(self):
        return reverse('city:unique_slug', args=[self.slug])

    def __str__(self):
        return self.name


class City(models.Model):
    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر'

    name = models.CharField('نام شهر', max_length=30)
    slug = models.SlugField('اسلاگ', max_length=40, allow_unicode=True, null=True)
    about = models.TextField('درباره شهر', null=True, blank=True)
    image = models.ImageField(upload_to='city', verbose_name='عکس', null=True, blank=True)
    population = models.CharField('جمعیت', max_length=20, null=True, blank=True)
    family = models.CharField('تعداد خانوار', max_length=20, null=True, blank=True)
    village = models.CharField('تعداد روستاها', max_length=20, null=True, blank=True)
    dialect = models.CharField('گویش', max_length=20, null=True, blank=True)

    # weather =
    # location =

    def __str__(self):
        return self.name


class Place(models.Model):
    class Meta:
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان'

    name = models.CharField(max_length=50, verbose_name='نام مکان', null=False)
    slug = models.SlugField('اسلاگ', max_length=40, allow_unicode=True, null=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(upload_to='place', verbose_name='عکس', null=True, blank=True)
    # category = models.CharField(max_length=1, choices=PLACE_CATEGORY, null=True, blank=True, verbose_name='دسته بندی')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')
    comments = GenericRelation('Comment')
    # location =
    pub_date = models.DateTimeField('تاریخ انتشار', auto_now_add=True, null=True, blank=True)
    views = models.ManyToManyField(IpClass, related_name='place_views', verbose_name='نمایش', blank=True)
    is_access = models.BooleanField('تأیید', default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city:place_details', args=[self.slug])

    def total_views(self):
        return self.views.count()


class PlaceImages(models.Model):
    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصویر'

    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='مکان')
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='place/place_images', verbose_name='تصویر')


class Soghat(models.Model):
    class Meta:
        verbose_name = 'سوغات'
        verbose_name_plural = 'سوغات'

    name = models.CharField(max_length=30, verbose_name='نام سوغات', null=False)
    slug = models.SlugField('اسلاگ', max_length=40, allow_unicode=True, null=True)
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='soghat', verbose_name='عکس', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')
    sub_category = models.CharField(max_length=1, choices=SOGHAT_CATEGORY, default='F', null=True, blank=True,
                                    verbose_name='زیر دسته بندی')
    pub_date = models.DateTimeField('تاریخ انتشار', auto_now_add=True, null=True, blank=True)
    is_access = models.BooleanField('تأیید', default=False)
    views = models.ManyToManyField(IpClass, related_name='soghat_views', verbose_name='نمایش', blank=True)
    comments = GenericRelation('Comment')

    def __str__(self):
        return '{} - {}'.format(self.name, self.sub_category)

    def get_absolute_url(self):
        return reverse('city:place_details', args=[self.slug])

    def total_views(self):
        return self.views.count()


class SoghatImages(models.Model):
    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصویر'

    soghat = models.ForeignKey(Soghat, on_delete=models.CASCADE, verbose_name='سوغات')
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='soghat/soghat_images', verbose_name='تصویر')


class Great(models.Model):
    class Meta:
        verbose_name = 'بزرگان'
        verbose_name_plural = 'بزرگان'

    name = models.CharField('نام و نام خانوادگی', max_length=50, null=False)
    slug = models.SlugField('اسلاگ', max_length=50, allow_unicode=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')
    father_name = models.CharField('نام پدر', max_length=30, null=True, blank=True)
    place_of_birth = models.CharField('محل تولد', max_length=50, null=True, blank=True)
    date_of_birth = models.CharField('تاریخ تولد', max_length=50, null=True, blank=True)
    date_of_death = models.CharField('تاریخ وفات', max_length=50, null=True, blank=True)
    post = models.CharField('سمت و مقام', max_length=50, null=True, blank=True)
    biography = models.TextField(verbose_name='زندگینامه', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(upload_to='great/images', verbose_name='عکس', null=True, blank=True)
    clip = models.FileField('کلیپ', upload_to='great/clips', null=True, blank=True)
    pub_date = models.DateTimeField('تاریخ انتشار', auto_now_add=True, null=True, blank=True)
    is_access = models.BooleanField('تأیید', default=False)
    views = models.ManyToManyField(IpClass, related_name='great_views', verbose_name='نمایش', blank=True)
    comments = GenericRelation('Comment')

    def __str__(self):
        return '{} - {}'.format(self.name, self.post)

    def total_views(self):
        return self.views.count()

    # def get_absolute_url(self):
    #     return reverse('city:great_details', args=[self.slug])


class GreatServices(models.Model):
    class Meta:
        verbose_name = 'خدمات بزرگان'
        verbose_name_plural = 'خدمات بزرگان'

    great = models.ForeignKey(Great, on_delete=models.CASCADE, verbose_name='نام بزرگ')
    service = models.CharField('خدمت', max_length=200)


class Martyrs(models.Model):
    class Meta:
        verbose_name = 'شهید'
        verbose_name_plural = 'شهدا'

    name = models.CharField('نام و نام خانوادگی', max_length=50, null=False)
    slug = models.SlugField('اسلاگ', max_length=50, allow_unicode=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')
    father_name = models.CharField('نام پدر', max_length=30, null=True, blank=True)
    place_of_birth = models.CharField('محل تولد', max_length=50, null=True, blank=True)
    date_of_birth = models.CharField('تاریخ تولد', max_length=50, null=True, blank=True)
    post = models.CharField('سمت و مقام', max_length=50, null=True, blank=True)
    place_of_death = models.CharField('محل شهادت', max_length=50, null=True, blank=True)
    date_of_death = models.CharField('تاریخ شهادت', max_length=50, null=True, blank=True)
    operation = models.CharField('عملیات', max_length=100, null=True, blank=True)
    biography = models.TextField(verbose_name='زندگینامه', null=True, blank=True)
    will = models.TextField(verbose_name='وصیت نامه', null=True, blank=True)
    image = models.ImageField(upload_to='martyrs/images', verbose_name='عکس', null=True, blank=True)
    clip = models.FileField('کلیپ', upload_to='martyrs/clips', null=True, blank=True)
    pub_date = models.DateTimeField('تاریخ انتشار', auto_now_add=True, null=True, blank=True)
    is_access = models.BooleanField('تأیید', default=False)
    views = models.ManyToManyField(IpClass, related_name='martyrs_views', verbose_name='نمایش', blank=True)
    comments = GenericRelation('Comment')

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.place_of_death, self.date_of_death)

    def get_absolute_url(self):
        return reverse('city:place_details', args=[self.slug])

    def total_views(self):
        return self.views.count()


class Hotel(models.Model):
    class Meta:
        verbose_name = 'هتل و رستوران'
        verbose_name_plural = 'هتل و رستوران'

    name = models.CharField('نام', max_length=50, null=False)
    slug = models.SlugField('اسلاگ', max_length=50, allow_unicode=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')
    sub_category = models.CharField(max_length=1, choices=HOTEL_RES_CATEGORY, null=True, blank=True,
                                    verbose_name='زیر دسته بندی')
    address = models.CharField('آدرس', max_length=100, null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    phone = models.CharField('تلفن', max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='hotel/images', verbose_name='عکس', null=True, blank=True)
    clip = models.FileField('کلیپ', upload_to='hotel/clips', null=True, blank=True)
    pub_date = models.DateTimeField('تاریخ انتشار', auto_now_add=True, null=True, blank=True)
    is_access = models.BooleanField('تأیید', default=False)
    views = models.ManyToManyField(IpClass, related_name='hotel_views', verbose_name='نمایش', blank=True)
    comments = GenericRelation('Comment')

    def __str__(self):
        return '{} - {}'.format(self.name, self.address)

    def get_absolute_url(self):
        return reverse('city:place_details', args=[self.slug])

    def total_views(self):
        return self.views.count()


class AttrHotel(models.Model):
    class Meta:
        verbose_name = 'ویژگی ها'
        verbose_name_plural = 'ویژگی'

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='نام هتل')
    attr = models.CharField('ویژگی', max_length=200)


class Comment(models.Model):
    class Meta:
        verbose_name = 'نظرات'
        verbose_name_plural = 'نظرات'

    fullname = models.CharField('نام و نام خانوادگی', max_length=40)
    email = models.EmailField('ایمیل')
    comment = models.TextField('نظر')
    data_add = models.DateTimeField('تاریخ انتشار', auto_now_add=True)
    confirm = models.BooleanField('تایید', default=False)
    likes = models.ManyToManyField(IpClass, related_name='likes', verbose_name='لایک', blank=True)
    dislikes = models.ManyToManyField(IpClass, related_name='dislikes', verbose_name='دیسلایک', blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, related_name='comments')
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        # return self.fullname
        return '{} - {} - {}'.format(self.content_object, self.fullname, self.object_id)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
