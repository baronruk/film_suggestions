import datetime

from django.core.exceptions import ValidationError

MIN_YEAR = 1999


def validate_preferred_year(value):
    current_year = datetime.datetime.now().year

    if not (MIN_YEAR <= value <= current_year):
        raise ValidationError(
            f"Preferred year must be between {MIN_YEAR} and {current_year}."
        )
    if len(str(value)) > 4:
        raise ValidationError("Preferred year cannot have more than 4 digits.")
