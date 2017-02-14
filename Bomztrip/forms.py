from dal import autocomplete
from search.models import *
from django import forms

def get_choice_list():
    cities = [i['city'] for i in Trip.objects.values('city')]
    countries = [i['country'] for i in Trip.objects.values('country')]
    continents = [i['continent'] for i in Trip.objects.values('continent')]
    total = cities + countries + continents
    final = []
    [final.append(item) for item in total if item not in final]
    return final

class SearchForm(forms.Form):
    keyword = autocomplete.Select2ListChoiceField(
        choice_list=get_choice_list,
        widget=autocomplete.ListSelect2(url='search-autocomplete'),
    )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['keyword'].label = ""
