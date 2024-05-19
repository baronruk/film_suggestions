from django.shortcuts import render

from .forms import SuggestionForm


def landing(request):
    form = SuggestionForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)

    context = {
        "form": form,
    }
    return render(request, "film_suggestions/landing.html", context)
