from django import forms
from news.models import News
from accounts.models import Profile, GENDER_CHOICES
from django.forms import ModelForm, Textarea
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.forms import UserChangeForm


class PostForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'slug', 'category', 'image', 'text', 'study_time')
        # widgets = {
        #     'title': Textarea(attrs={'cols': 80, 'rows': 1, 'class': 'p-1'}),
        #     'slug': Textarea(attrs={'cols': 80, 'rows': 1, 'class': 'p-1'}),
        # }


class MyUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email']

    first_name = forms.CharField(label='نام', max_length=50,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'rounded border border-gray-300 w-full text-gray-800 mt-4 '
                                                  'mb-8 px-3 py-2 block'}))

    last_name = forms.CharField(label='نام خانوادگی', max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'rounded border border-gray-300 w-full text-gray-800 mt-4 '
                                                 'mb-8 px-3 py-2 block'}))
    email = forms.CharField(label='ایمیل', max_length=50,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'rounded border border-gray-300 text-gray-800 w-full mt-4 '
                                             'mb-8 px-3 py-2 block'}))

    password = None


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'gender', 'address', 'profile_image']

    mobile = forms.CharField(label='موبایل', max_length=50,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'rounded border border-gray-300 w-full text-gray-800 mt-4 '
                                              'mb-8 px-3 py-2 block'}))

    gender = forms.CharField(label='جنسیت', max_length=50,
                             widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'rounded border '
                                                                                         'border-gray-300 mt-4 '
                                                                                         'mb-8 block '
                                                                                         ' text-gray-800'}))
    address = forms.CharField(label='آدرس', max_length=50,
                              widget=forms.Textarea(
                                  attrs={'class': 'rounded border border-gray-300  text-gray-800 w-full '
                                                  ' mt-4 mb-8 px-3 py-2 block'}))

    profile_image = forms.FileInput()
