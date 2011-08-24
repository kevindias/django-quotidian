from django.test import TestCase

from quotidian import models

class QuoteModelTests(TestCase):
    """
    Tests for the Quote model and manager.

    """
    fixtures = ['test_data.json']

    def test_random_public_only(self):
        """
        Only quotes marked as public should be returned by get_random.

        """
        # Delete all public quotes
        public_quotes = models.Quote.objects.filter(public=True)
        public_quotes.delete()
        # Insert a non-public quote so we know there's at least one stored
        models.Quote.objects.create(source='Test Source', content='Test Content', public=False)
        # None of the quotes should be public, so this should be empty
        self.assertEqual(len(models.Quote.objects.get_random()), 0)
