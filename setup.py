import setuptools

long_description = open('README.rst').read()

setuptools.setup(
  name = 'lcboapi',
  version = '0.2.1',
  author = 'Shane Martin',
  author_email = 'dev.sh@nemart.in',
  description = 'Python wrapper for the unofficial LCBO API',
  long_description = long_description,
  url = 'https://github.com/shamrt/LCBOAPI',
  packages=setuptools.find_packages(),
  license='MIT License',
  download_url = 'https://github.com/shamrt/LCBOAPI/archive/v0.2.1.tar.gz',
  keywords = ['api', 'lcbo'],
  classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
