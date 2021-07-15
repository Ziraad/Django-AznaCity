from django import forms

from city.models import Place, Soghat, SOGHAT_CATEGORY, Hotel, HOTEL_RES_CATEGORY


class AddPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'image', 'description')

    name = forms.CharField(label='نام', max_length=50,
                           widget=forms.TextInput(
                               attrs={'class': 'rounded border border-gray-300 text-gray-800 w-full mt-4 '
                                               'mb-8 px-3 py-2 block'}))

    description = forms.CharField(label='توضیحات',
                                  widget=forms.Textarea(
                                      attrs={'class': 'rounded border border-gray-300 w-full '
                                                      'text-gray-800 mt-4 mb-8 '
                                                      'px-3 py-2 block'}))
    image = forms.CharField(label='عکس', max_length=50,
                            widget=forms.FileInput(
                                attrs={'class': 'mt-4 mb-8 block'}))


class AddSoghatForm(forms.ModelForm):
    class Meta:
        model = Soghat
        fields = ('name', 'description', 'image', 'sub_category')

    name = forms.CharField(label='نام', max_length=50,
                           widget=forms.TextInput(
                               attrs={'class': 'rounded border border-gray-300  text-gray-800 w-full mt-4 '
                                               'mb-8 px-3 py-2 block'}))

    description = forms.CharField(label='توضیحات',
                                  widget=forms.Textarea(
                                      attrs={'class': 'rounded border border-gray-300 w-full  '
                                                      'text-gray-800 mt-4 mb-8 '
                                                      'px-3 py-2 block'}))
    image = forms.CharField(label='عکس', max_length=50,
                            widget=forms.FileInput(
                                attrs={'class': 'mt-4 mb-8 block'}))

    sub_category = forms.CharField(label='دسته بندی', max_length=50,
                                   widget=forms.Select(choices=SOGHAT_CATEGORY, attrs={'class': 'rounded border '
                                                                                                'border-gray-300 mt-4 '
                                                                                                'mb-8 block '
                                                                                                ' text-gray-800'}))


class AddHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('name', 'image', 'sub_category', 'phone', 'address', 'description')

    name = forms.CharField(label='نام', max_length=50,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'rounded border border-gray-300 text-gray-800 w-full mt-4 '
                                            'mb-8 px-3 py-2 block'}))

    description = forms.CharField(label='توضیحات',
                                  widget=forms.Textarea(
                                      attrs={'class': 'rounded border border-gray-300 w-full  '
                                                      'text-gray-800 mt-4 mb-8 '
                                                      'px-3 py-2 block'}))
    image = forms.CharField(label='عکس', max_length=50,
                            widget=forms.FileInput(
                                attrs={'class': 'mt-4 mb-8 block'}))

    sub_category = forms.CharField(label='دسته بندی', max_length=50,
                                   widget=forms.Select(choices=HOTEL_RES_CATEGORY,
                                                       attrs={'class': 'rounded border border-gray-300 mt-4 '
                                                                       'mb-8 block  text-gray-800'}))
    address = forms.CharField(label='آدرس', max_length=50,
                              widget=forms.Textarea(
                                  attrs={'class': 'rounded border border-gray-300  text-gray-800 w-full '
                                                  'md:w-96 mt-4 mb-8 px-3 py-2 block'}))
    phone = forms.CharField(label='تلفن', max_length=50,
                            widget=forms.TextInput(
                                attrs={'class': 'rounded border border-gray-300  text-gray-800 w-full '
                                                'md:w-96 mt-4 mb-8 px-3 py-2 block'}))


class CommentForm(forms.Form):
    fields = ('fullname', 'email', 'comment')

    fullname = forms.CharField(label='نام و نام خانوادگی', required=False, max_length=50,
                               widget=forms.TextInput(
                                   attrs={'class': 'rounded border border-gray-300 text-gray-800 '
                                                   'mt-4 mb-8 px-3 py-2 text-sm w-full block'}))
    email = forms.EmailField(label='ایمیل', max_length=50, required=False,
                             widget=forms.TextInput(attrs={'class': 'rounded border border-gray-300 '
                                                                    'text-gray-800  mt-4 mb-8 px-3 py-2 '
                                                                    'text-sm w-full block'}))
    # phone = forms.CharField(label='موبایل', max_length=11, required=True,
    #                         widget=forms.TextInput(attrs={'class': 'rounded border border-gray-300 '
    #                                                                'text-gray-800  mt-4 mb-8 px-3 py-2 '
    #                                                                'text-sm w-full block'}))
    comment = forms.CharField(label='متن پیام', required=True,
                              widget=forms.Textarea(
                                  attrs={'class': 'rounded border border-gray-300 '
                                                  'text-gray-800 mt-4 mb-8 '
                                                  'px-3 py-2 w-full block'}))

# 'placeholder': 'لطفاً نام خود را وارد نمایید'
# 'placeholder': 'لطفاً ایمیل خود را وارد نمایید'
# 'placeholder': 'لطفاً شماره همراه خود را وارد نمایید'
