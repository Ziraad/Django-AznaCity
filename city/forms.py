from django import forms

from city.models import Place


class AddForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'description', 'image')

    name = forms.CharField(label='نام', max_length=50,
                           widget=forms.TextInput(
                               attrs={'class': 'rounded border border-gray-100 bg-gray-100 text-gray-800 w-full mt-4 '
                                               'mb-8 px-3 py-2 block'}))

    description = forms.CharField(label='توضیحات',
                                  widget=forms.Textarea(
                                      attrs={'class': 'rounded border border-gray-100 w-full bg-gray-100 '
                                                      'text-gray-800 mt-4 mb-8 '
                                                      'px-3 py-2 block'}))
    image = forms.CharField(label='عکس', max_length=50,
                            widget=forms.FileInput(
                                attrs={'class': 'mt-4 mb-8 block'}))
