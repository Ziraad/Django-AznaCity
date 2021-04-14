from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

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
    body = RichTextUploadingField('توضیحات')

    def get_absolute_url(self):
        return reverse('city:unique_slug', args=[self.slug])

    def __str__(self):
        return self.name


class City(models.Model):
    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر'

    name = models.CharField(max_length=30, verbose_name='نام شهر')
    slug = models.SlugField('اسلاگ', max_length=40, allow_unicode=True, null=True)
    about = models.TextField(verbose_name='درباره شهر', null=True, blank=True)
    image = models.ImageField(upload_to='city', verbose_name='عکس', null=True, blank=True)
    dialect = models.CharField(max_length=20, verbose_name='گویش', null=True, blank=True)
    # weather =
    # location =

    def __str__(self):
        return self.name


class Place(models.Model):
    class Meta:
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان'

    name = models.CharField(max_length=50, verbose_name='نام مکان')
    slug = models.SlugField('اسلاگ', max_length=40, allow_unicode=True, null=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(upload_to='place', verbose_name='عکس', null=True, blank=True)
    # category = models.CharField(max_length=1, choices=PLACE_CATEGORY, null=True, blank=True, verbose_name='دسته بندی')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')
    # location =

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city:place_details', args=[self.slug])


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

    name = models.CharField(max_length=30, verbose_name='نام سوغات')
    slug = models.SlugField('اسلاگ', max_length=40, allow_unicode=True, null=True)
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='soghat', verbose_name='عکس', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')
    sub_category = models.CharField(max_length=1, choices=SOGHAT_CATEGORY, default='F', null=True, blank=True, verbose_name='زیر دسته بندی')

    def __str__(self):
        return '{} - {}'.format(self.name, self.category2)

    def get_absolute_url(self):
        return reverse('city:place_details', args=[self.slug])


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

    name = models.CharField('نام و نام خانوادگی', max_length=50)
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

    def __str__(self):
        return '{} - {}'.format(self.name, self.post)

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

    name = models.CharField('نام و نام خانوادگی', max_length=50)
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

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.place_of_death, self.date_of_death)

    # def get_absolute_url(self):
    #     return reverse('city:martyrs_details', args=[self.slug])


class Hotel(models.Model):
    class Meta:
        verbose_name = 'هتل و رستوران'
        verbose_name_plural = 'هتل و رستوران'

    name = models.CharField('نام', max_length=50)
    slug = models.SlugField('اسلاگ', max_length=50, allow_unicode=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')
    sub_category = models.CharField(max_length=1, choices=HOTEL_RES_CATEGORY, null=True, blank=True, verbose_name='زیر دسته بندی')
    address = models.CharField('آدرس', max_length=100, null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    phone = models.CharField('تلفن', max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='hotel/images', verbose_name='عکس', null=True, blank=True)
    clip = models.FileField('کلیپ', upload_to='hotel/clips', null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.address)

    def get_absolute_url(self):
        return reverse('city:place_details', args=[self.slug])


class AttrHotel(models.Model):
    class Meta:
        verbose_name = 'ویژگی ها'
        verbose_name_plural = 'ویژگی'

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='نام هتل')
    attr = models.CharField('ویژگی', max_length=200)