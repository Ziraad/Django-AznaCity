from django.contrib import admin

from .models import City, Place, Soghat, Category, Martyrs, GreatServices, Great, PlaceImages, SoghatImages, AttrHotel, \
    Hotel

admin.site.register(City)


# Category Model-------------------------------------------------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Place Model-------------------------------------------------------------------
class PlaceImgInline(admin.TabularInline):
    model = PlaceImages
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_access', 'category']
    list_editable = ['category', 'is_access']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PlaceImgInline]
    actions = ['approve_comments', 'dont_approve_comments']

    def approve_comments(self, request, queryset):
        result = queryset.update(is_access=True)
        self.message_user(request, '{} مکان با موفقیت تغیر یافت.'.format(result))

    def dont_approve_comments(self, request, queryset):
        result = queryset.update(is_access=False)
        self.message_user(request, '{} مکان با موفقیت تغیر یافت.'.format(result))

    approve_comments.short_description = 'تأیید مکانهای انتخاب شده'
    dont_approve_comments.short_description = 'عدم تأیید مکانهای انتخاب شده'


# Soghat Model-------------------------------------------------------------------
class SoghatImgInline(admin.TabularInline):
    model = SoghatImages
    extra = 1


@admin.register(Soghat)
class SoghatAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_access']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SoghatImgInline]

    actions = ['approve_comments', 'dont_approve_comments']

    def approve_comments(self, request, queryset):
        result = queryset.update(is_access=True)
        self.message_user(request, '{} سوغات با موفقیت تغیر یافت.'.format(result))

    def dont_approve_comments(self, request, queryset):
        result = queryset.update(is_access=False)
        self.message_user(request, '{} سوغات با موفقیت تغیر یافت.'.format(result))

    approve_comments.short_description = 'تأیید گزینه های انتخاب شده'
    dont_approve_comments.short_description = 'عدم تأیید گزینه های انتخاب شده'


# Great Model-------------------------------------------------------------------
class GreatSerInline(admin.TabularInline):
    model = GreatServices
    extra = 1


@admin.register(Great)
class GreatAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_access']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GreatSerInline]

    actions = ['approve_comments', 'dont_approve_comments']

    def approve_comments(self, request, queryset):
        result = queryset.update(is_access=True)
        self.message_user(request, '{} گزینه با موفقیت تغیر یافت.'.format(result))

    def dont_approve_comments(self, request, queryset):
        result = queryset.update(is_access=False)
        self.message_user(request, '{} گزینه با موفقیت تغیر یافت.'.format(result))

    approve_comments.short_description = 'تأیید گزینه های انتخاب شده'
    dont_approve_comments.short_description = 'عدم تأیید گزینه های انتخاب شده'


# Martyrs Model-------------------------------------------------------------------
@admin.register(Martyrs)
class MartyrsAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_access']
    prepopulated_fields = {'slug': ('name',)}

    actions = ['approve_comments', 'dont_approve_comments']

    def approve_comments(self, request, queryset):
        result = queryset.update(is_access=True)
        self.message_user(request, '{} گزینه با موفقیت تغیر یافت.'.format(result))

    def dont_approve_comments(self, request, queryset):
        result = queryset.update(is_access=False)
        self.message_user(request, '{} گزینه با موفقیت تغیر یافت.'.format(result))

    approve_comments.short_description = 'تأیید گزینه های انتخاب شده'
    dont_approve_comments.short_description = 'عدم تأیید گزینه های انتخاب شده'


# Hotel Model-------------------------------------------------------------------
class HotelAttrInline(admin.TabularInline):
    model = AttrHotel
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_access']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [HotelAttrInline]

    actions = ['approve_comments', 'dont_approve_comments']

    def approve_comments(self, request, queryset):
        result = queryset.update(is_access=True)
        self.message_user(request, '{} هتل با موفقیت تغیر یافت.'.format(result))

    def dont_approve_comments(self, request, queryset):
        result = queryset.update(is_access=False)
        self.message_user(request, '{} هتل با موفقیت تغیر یافت.'.format(result))

    approve_comments.short_description = 'تأیید گزینه های انتخاب شده'
    dont_approve_comments.short_description = 'عدم تأیید گزینه های انتخاب شده'
