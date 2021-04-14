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
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PlaceImgInline]


# Soghat Model-------------------------------------------------------------------
class SoghatImgInline(admin.TabularInline):
    model = SoghatImages
    extra = 1


@admin.register(Soghat)
class SoghatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SoghatImgInline]


# Great Model-------------------------------------------------------------------
class GreatSerInline(admin.TabularInline):
    model = GreatServices
    extra = 1


@admin.register(Great)
class GreatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GreatSerInline]


# Martyrs Model-------------------------------------------------------------------
@admin.register(Martyrs)
class MartyrsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Hotel Model-------------------------------------------------------------------
class HotelAttrInline(admin.TabularInline):
    model = AttrHotel
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [HotelAttrInline]
