from django import forms

from .constants import FilmTypeChoices, GenreChoices
from .validators import validate_preferred_year


class SuggestionForm(forms.Form):
    film_type = forms.ChoiceField(
        choices=FilmTypeChoices.choices, widget=forms.RadioSelect
    )
    genre = forms.ChoiceField(choices=GenreChoices.choices, widget=forms.Select)
    release_year = forms.IntegerField(
        required=False, validators=[validate_preferred_year]
    )
    preffered_actors = forms.CharField(
        required=False,
        widget=forms.Textarea,
        help_text="Names must be comma seperated",
    )
    preffered_directors = forms.CharField(
        required=False,
        widget=forms.Textarea,
        help_text="Names must be comma seperated",
    )
