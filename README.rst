
================ 
local_databricks 
================


Python library that provides a set of functions for handling running notebooks both locally and in Databricks using the same commands.


Installation
------------

there are two options to install the package


Cloning from repository
~~~~~~~~~~~~~~~~~~~~~~~

The package can be installed using poetry

.. code-block:: console

    $ git clone link-to-repository
    $ cd local_databricks
    $ python -m venv .venv
    $ poetry install


Or using ``setup.py`` file

.. code-block:: console

    $ git clone link-to-repository
    $ cd local_databricks
    $ python -m venv .venv
    $ python setup.py install


Installation from private PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the package was published as an `Azure Artifact <https://docs.microsoft.com/en-us/azure/devops/artifacts/quickstarts/python-packages?view=azure-devops>`__
you can install it using ``pip`` or other package manager as ``pipenv`` or ``poetry``. You need the ``ArtifactFeedName``, the ``ArtifactUrl`` and the ``AccessToken``
given by whoever has administrator permissions on the project, and then

.. code-block:: console

    $ pip install --extra-index-url "https://ArtifactFeedName:AccessToken@ArtifactUrl"
