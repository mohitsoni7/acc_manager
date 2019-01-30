from django import template

register = template.Library()

@register.filter(name='cal')
def cal(qty, rate):
    return int(qty * rate)
