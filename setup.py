import sys
from codecs import open  # To use a consistent encoding
from os import path

# Always prefer setuptools over distutils
from setuptools import (setup, find_packages)

here = path.abspath(path.dirname(__file__))
install_requirements = [
    # Place your project requirements here.

    # One way to keep up-to-date while still keeping a stable API is to
    # use semantic versioning. If the requirement has a major.minor.[bugfix] format,
    # then you can restrict versions by range. Suggest you read
    # `PEP 440<https://www.python.org/dev/peps/pep-0440/>`_ for more information.

    # Example where we ask for a ``fake`` library and block a specific version.
    # 'fake>=1.0.0, !1.1.0, <2.0.0a0'
]

# The following are meant to avoid accidental upload/registration of this
# package in the Python Package Index (PyPi)
pypi_operations = frozenset(['register', 'upload']) & frozenset([x.lower() for x in sys.argv])
if pypi_operations:
    raise ValueError('Command(s) {} disabled in this example.'.format(', '.join(pypi_operations)))

# Python favors using README.rst files (as opposed to README.md files)
# If you wish to use README.md, you must add the following line to your MANIFEST.in file::
#
#     include README.md
#
# then you can change the README.rst to README.md below.
with open(path.join(here, 'README.rst'), encoding='utf-8') as fh:
    long_description = fh.read()

# We separate the version into a separate file so we can let people
# import everything in their __init__.py without causing ImportError.
__version__ = None
exec(open('module_template/about.py').read())
if __version__ is None:
    raise IOError('about.py in project lacks __version__!')

setup(name='module_template', version=__version__,
      author='Ben Jolitz',
      description='Template for creating python modules',
      long_description=long_description,
      license='BSD',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      include_package_data=True,
      # This part is good for when the setup.py itself cannot proceed until dependencies
      # in ``setup_requires`` are met. If you also need some/all of the dependencies in
      # ``setup_requires`` to run your module, be sure to have them in the install_requirements to.
      # setup_requires=[],
      #
      # You may specify additional packages for a more feature filled install.
      # Example of a extras_require where one has to do:
      #     python -m pip install module_template    (to get the default package)
      #     python -m pip install module_template[test]   (to get additional dependencies
      #                                                    to enable ``test`` functionality)
      #     python -m pip install module_template[test,fast] (same as above, except with the
      #                                                       ``fast`` dependencies for that
      #                                                       functionality)
      #
      # extras_require= {
      #     'test': ['unittest2'],
      #     'fast': ['hiredis', 'ujson']
      # },
      #
      # Sometimes one has an external package hosted somewhere else
      #    (*cough* mysql-connector-python *cough*) and you want everything
      #    be installed in one pass using ``pip``. You can specify the name
      #    of the dependency, where to get it and what the name of the package
      #    should be if the download uri is different. The URI must be something
      #    compatible with a ``pip install`` (i.e. ``pip instal http://localhost/package.zip``)
      #
      # You will have to install this package with the ``--process-dependency-links`` pip option
      # specified.
      # dependency_links=[
      #       "https://localhost:8080/test/path/file.zip#egg=package_name_underscore-1.2.3"
      # ],
      install_requires=install_requirements,
      keywords=['module', 'template', 'library'],
      url="https://github.com/benjolitz/module_template",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
      ])
