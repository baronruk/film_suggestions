from django.template import Library

register = Library()


@register.inclusion_tag("film_suggestions/tags/field.html")
def render_field(field):
    return {
        "field": field,
    }
