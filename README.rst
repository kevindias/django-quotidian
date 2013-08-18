Text snippets for Django templates
==================================

Summary
-------

This very simple application provides a way to stick a "quote" object into
the context of your `Django <https://www.djangoproject.com/>`_ templates. Quotes are selected at random from
the quotidian_quote database table ignoring any rows with the "public" field
set to False.


Installing django-quotidian
---------------------------

There are several ways to install this application.

Using pip or easy_install
^^^^^^^^^^^^^^^^^^^^^^^^^

Pip is the recommended package-installation tool for Python. To install
django-quotidian with pip, use the command::

    pip install django-quotidian

If you prefer to use easy_install then replace ``pip`` with ``easy_install``
in the above command.

To install the latest in-development version (which may not be stable) directly
from the project's Git repository you can use the command::

    pip install -e git+ssh://git@bitbucket.org/dias.kev/django-quotidian#egg=quotidian

Using setuptools
^^^^^^^^^^^^^^^^

Download the package source code or distribution tarball and then run the
following command in the django-quotidian directory::

    python setup.py install


Using django-quotidian
----------------------

1. Install django-quotidian as described above.
2. Create the quotidian_quote database table using manage.py syncdb.
3. Populate the new database table with whatever quotations, testimonials,
   hints, tips or snippets you want to use.
4. Add "quotidian" to your project's INSTALLED_APPS setting.
5. You can now choose between using quotidian's context processor or template
   tag, or both.

Context processor
^^^^^^^^^^^^^^^^^

This adds a variable named "quotidian_quote" with the attributes described in
the 'Quote object attributes' section to the template context of every request.

Add 'quotidian.context_processors.random_public_quote' to your project's
TEMPLATE_CONTEXT_PROCESSORS setting to activate the context processor.

Template tag
^^^^^^^^^^^^

If you only want to use quotidian on a few pages of your site and don't want
the overhead of running the context processor for every request then use
quotidian's template tag instead. This also lets you add filters to select
specific quotes or inlcude multiple quotes on a page, things you can't do with
the context processor.

To use the template tag, load the quotidian template library with
``{% load quotidian_tags %}`` at the top of your template. You can then inlcude 
a quote on your page by using the ``{% random_quote %}`` tag. 

You can override ``templates/quotidian/quotidian_quote.html`` if you need to
customize the quote's template fragment.

The 'random_quote' tag accepts keyword arguments in the same format as Django's
queryset filter method which are used to restrict the pool of quotes quotidian
selects from. For example, use ``{% random_quote source__contains='John' %}`` to
select a random quote from all (public) quotes with a source containing the
string 'John'.


Quote object attributes
-----------------------

id
    The quote's database primary key.

source
    Intended as a short attribution for the quote's contents.

content
    The actual text of the quote.

detailed_citation
    Can be used for additional attribution.

public
    A boolean flag controlling whether the quote should be considered public
    or not. Currently only public quotes will be selected.

created
    The quote's creation timestamp.

modified
    The quote's last modified timestamp.


Reporting problems or suggesting improvements
---------------------------------------------

Please use the issue tracker at the project's Bitbucket repository:
https://bitbucket.org/dias.kev/django-quotidian
