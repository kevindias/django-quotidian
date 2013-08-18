from setuptools import setup


setup(name='django-quotidian',
      version='0.2.1',
      author='Kevin Dias',
      author_email='kevin@kevindias.com',
      url='http://kevindias.com/projects/quotidian/',
      description='Adds snippets of text to your Django templates.',
      packages=['quotidian'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django',
                   'Topic :: Utilities'],
      zip_safe=False,
)
