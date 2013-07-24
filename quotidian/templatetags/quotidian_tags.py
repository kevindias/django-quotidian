from django import template

from quotidian.models import Quote


register = template.Library()

@register.inclusion_tag('quotidian/quotidian_quote.html')
def random_quote():
    quote = Quote.objects.get_random()
    return {'random_quote': quote}
