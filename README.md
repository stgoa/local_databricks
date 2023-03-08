# local_databricks
```local_databricks``` is a Python library that provides a set of functions for handling running notebooks both locally and in Databricks using the same commands. It aims to simplify the development process by allowing developers to use a consistent interface, regardless of where the notebook is running.

This can be used to test Databricks pipelines locally.

## Instalation
To install local_databricks, there are two options:

**Cloning from repository**

The package can be installed using poetry

```
    $ git clone link-to-repository
    $ cd local_databricks
    $ python -m venv .venv
    $ poetry install
```

or using ``setup.py`` file

```

    $ git clone link-to-repository
    $ cd local_databricks
    $ python -m venv .venv
    $ python setup.py install
```

**PIP**

```TODO```


## Usage
To use local_databricks, you first need to authenticate with Databricks. You can do this by setting the following environment variables:

```TODO```

You can then import the local_databricks module and use its functions to interact with Databricks:


```
# refactor your databricks notebooks with the following:

# import the library
from local_databricks.ldbutils import notebook

# to run a notebook
# instead of dbutils.notebook.run(path, timeout_seconds, arguments=arguments)
# replace with 
notebook.run_notebook(path = path, timeout_seconds = timeout_seconds, arguments = arguments)

# to access to secrets
# instead of dbutils.secrets.get(scope=scope, key=key)
# replace with
notebook.get_secret(scope = scope, key = key)

# to access to enviroment variables
# instead of spark.conf.get(key=key)
# replace with
notebook.read_enviroment(key = key)

# to set enviroment variables
# instead of spark.conf.set(key, value)
# replace with
notebook.set_enviroment(key = key, value=value)

# to display objects
# instead of display(obj)
# replace with
notebook.display(obj)

```

## Features

TODO:
1. Handling secrets
2. Reading/defining enviroment variables
3. Read/write spark dataframes
4. Excecute notebooks passings parameters
5. Connection with external databases


## Contributing

If you'd like to contribute to local_databricks, please fork the repository and make your changes in a new branch. Once you've made your changes, submit a pull request and we'll review your changes.


License
local_databricks is licensed under the GNU License. See LICENSE for more information.
