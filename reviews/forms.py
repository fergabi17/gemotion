from django import forms


class ReviewForm(forms.Form):
    CHOICES = (('1', 'I Played it',), ('0', 'I Watched it',))
    pk_list = forms.CharField(widget=forms.TextInput(attrs={'id':'pk-list'}))
    played = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'btn btn-secondary'}), label="", choices=CHOICES)

    