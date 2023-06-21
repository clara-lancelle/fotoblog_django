# blog/templatetags/blog_extras.py
from django import template
from django.utils import timezone

register = template.Library()

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
 
@register.filter
def model_type(value):
    return type(value).__name__

@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'vous'
    return user.username

@register.filter
def get_posted_at_display(time):
    second_ago = (timezone.now() - time).total_seconds()
    if second_ago <= HOUR:
        return f'Publié il y a {int(second_ago // MINUTE)} minutes.'
    elif second_ago <= DAY:
        return f'Publié il y a {int(second_ago // HOUR)} heures.'
    return f'Publié le {time.strftime("%d %b %y à %Hh%M")}'
