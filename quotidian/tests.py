from django.test import TestCase

from quotidian.models import Quote

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
        public_quotes = Quote.objects.filter(public=True)
        public_quotes.delete()
        # Insert a non-public quote so we know there's at least one stored
        Quote.objects.create(source='Test Source',
                             content='Test Content',
                             public=False)
        # None of the quotes should be public, so this should be empty
        self.assertEqual(len(Quote.objects.get_random()), 0)

    def test_kwarg_filters(self):
        """
        Tests additional filters for Quote.objects.get_random().
        
        """
        filter_detail = Quote.objects.get_random(detailed_citation='Detail3')
        filter_source = Quote.objects.get_random(source='Source3')
        self.assertEqual(filter_detail, filter_source)

        filter_date = Quote.objects.get_random(public=False,
                                               created__gte='2011-08-23 15:08:50',
                                               created__lte='2011-08-23 15:08:59')
        filter_content = Quote.objects.get_random(public=False,
                                                    content='Content2')
        self.assertEqual(filter_date, filter_content)
