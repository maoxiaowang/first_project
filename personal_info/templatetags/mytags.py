from functools import reduce

from django import template

register = template.Library()


@register.filter(is_safe=False)
def add_filter(value, rounded=2):
    assert isinstance(value, list)
    return round(sum(value), rounded)


@register.simple_tag
def add_tag(*args, **kwargs):
    args = args[0]
    assert isinstance(args, list)
    result = reduce(lambda x, y: x+y, args)
    rounded = kwargs.get('rounded')
    rounded = rounded or 2
    result = round(result, rounded)
    return result


@register.filter
def label_class(value, cls):
    return value.label_tag(attrs={'class': cls})
