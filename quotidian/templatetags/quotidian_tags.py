from django import template

from quotidian.models import Quote


register = template.Library()

@register.inclusion_tag('quotidian/quotidian_quote.html')
def random_quote(**kwargs):
    quote = Quote.objects.get_random(**kwargs)
    return {'random_quote': quote}
