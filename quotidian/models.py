from random import randint

from django.db import models


class QuoteManager(models.Manager):
    def get_random(self, **kwargs):
        """
        Returns a 'random' (optionally filtered) quote.

        This method of retreiving a random record is used instead of Django's
        order_by('?') because of how slow that can be for some databases.

        """
        filters = {'public': True}
        filters.update(**kwargs)
        quotes = self.filter(**filters)


        num_quotes = quotes.count()
        try:
            random_offset = randint(0, num_quotes - 1)
            quote = quotes[random_offset]
        except ValueError:
            quote = self.none()
        return quote


class Quote(models.Model):
    """
    Quotes and their sources.

    """
    id = models.AutoField(primary_key=True, db_column='quote_id')
    source = models.CharField(max_length=250)
    content = models.TextField()
    detailed_citation = models.CharField(max_length=500, default='', blank=True)
    public = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = QuoteManager()

    def __unicode__(self):
        return self.content
