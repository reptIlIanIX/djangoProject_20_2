from django import template

register = template.Library()


@register.filter
def my_image(image):
    if image:
        return f'/media/{image}'
    return ''


@register.simple_tag
def mediapath(image):
    if image:
        return f'media/{image}'
    return ''
