from quotidian.models import Quote


def random_public_quote(request):
    """
    Returns context dict containing a single quote.

    This is chosen from amongst quotes flagged as public.

    """
    quote = Quote.objects.get_random()
    return {'random_quote': quote}
