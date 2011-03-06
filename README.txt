Text snippets for Django templates
==================================

Summary
-------

This very simple application provides a way to stick a "quote" object into
the context of your [Django][1] templates. Quotes are currently selected at
random from the quotidian_quote database table ignoring any rows with the "public"
field set to False.

[1]: http://www.djangoproject.com/ "Django Project"


Installing django-quotidian
---------------------------

There are several ways to install this application.

You can run the following command in the django-quotidian directory:

    python setup.py install

You can also put the included quotidian directory on your Python path,
or symlink to it from somewhere on your Python path.


Using django-quotidian
----------------------

1. Install django-quotidian as described above.
2. Create the quotidian_quote database table using manage.py syncdb.
3. Populate the new database table with whatever quotations, testimonials,
   hints, tips or snippets you want to use.
4. Add 'quotidian' to your project's INSTALLED_APPS setting.
5. Add 'quotidian.context_processors.random_public_quote' to your project's
   TEMPLATE_CONTEXT_PROCESSORS setting.

Your template context will now include a variable named "a-quote" with the
following attributes:

* id                - The quote's database primary key.
* source            - Intended as a short attribution for the quote's contents.
* content           - The actual text of the quote.
* detailed_citation - Can be used for additional attribution.
* public            - A boolean flag controlling whether the quote should be
                      considered public or not. Currently only public quotes
                      will be selected.
* created           - The quote's creation timestamp.
* modified          - The quote's last modified timestamp.


Reporting problems or suggesting improvements
---------------------------------------------

Please use the issue tracker at the project's Bitbucket repository: [https://bitbucket.org/dias.kev/django-quotidian]
