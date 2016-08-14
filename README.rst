Template for defining Python modules
-------------------------------------

This is a template designed to make it quick to bootstrap an installable Python module for private and professional purposes. It is based upon several issues and patterns I've experienced in deploying Python services and libraries.

Python's unit of software distribution is a module. Most modules will have a ``setup.py`` or a ``setup.cfg`` defined. This approach has the following benefits:

    - dependencies can be declared and automatically installed/upgraded
    - one doesn't need to ``cd`` to a specific directory to start a service
    - Easy upgrade path
        + No issues with stale ``.pyc`` files


Python modules can create source distributions (``sdist``) and binary distributions (``bdist_wheel``). This plays very nicely with a PyPI mirror, which allows for complex projects to be installed/updated on a routine basis.

There are several key points in a pain-free install:
    - setup.py
    - MANIFEST.in (necessary if you have non-Python files in your project)
    - README.rst (README.md will require you to add README.md to MANIFEST.in)

In addition, you are suggested to follow the basic structure of ``module_template``.

Please note that ``module_template`` is just a name and you can freely rename it to reflect your
wishes. Just be sure to update your ``setup.py``, your ``about.py`` and (if you have it defined) a ``MANIFEST.in``

--------------------------
Expected Behavior
--------------------------

It is expected that all your business logic and assets will be in your project folder (currently named ``module_template`` with an ``__init__.py`` defined).

----------------------------
Including non Python files
----------------------------

``find_packages()`` will create a file listing for an install by looking for ``__init__.py`` files. 

In that case, you want a MANIFEST.in to graft those folders into the finalized modular installation.

Please see MANIFEST.in for more details.