import ast
import json

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from openai import OpenAI

from .forms import SuggestionForm
from .helpers import sign, unsign


def landing(request):
    form = SuggestionForm(request.POST or None)

    if form.is_valid():
        signed_data = sign("film_suggestions", form.cleaned_data)
        return HttpResponseRedirect(reverse("recommendations", args=(signed_data,)))

    context = {
        "form": form,
    }
    return render(request, "film_suggestions/landing.html", context)


def recommendations(request, signed_data):
    # unsign the signed data string
    data_str = unsign("film_suggestions", signed_data)
    # convert the string representation of the data to a dictionary
    data = ast.literal_eval(data_str)

    # extract values from the data dictionary
    film_type = data.get("film_type", None)
    genre = data.get("genre", None)
    release_year = data.get("release_year", None)
    preferred_actors = data.get("preferred_actors", None)
    preferred_directors = data.get("directors", None)

    # create an OpenAI client
    client = OpenAI(
        api_key=settings.OPENAI_API_KEY,
    )

    # construct a user message with the extracted data
    user_message = (
        f"Film Type: {film_type}, Genre:{genre}, Release Year: {release_year},"
        + f"Preferred Actors:[{preferred_actors}], Preferred directors:[{preferred_directors}]"
    )

    # generate a response from the OpenAI GPT-4 model
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        max_tokens=7192,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that makes recommendations based on "
                + "strictly existing films,series."
                + "Output JSON:recommendations:title,year or error.",
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
    )

    # convert the response to dictionary and extract the content from the response
    dict_response = response.to_dict()
    content = dict_response["choices"][0]["message"]["content"]

    # parse JSON string
    context = {
        "results": json.loads(content),
    }

    return render(request, "film_suggestions/results.html", context)
