# custom_filters.py
from django import template
from datetime import datetime

register = template.Library()

@register.filter
def to_datetime(date_str):
    try:
        return datetime.strptime(date_str, '%d %B %Y г. %H:%M')
    except ValueError:
        return None
