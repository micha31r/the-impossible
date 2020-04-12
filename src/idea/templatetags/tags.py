from django import template

register = template.Library()

@register.filter(name="times")
def times(value):
	return range(value)