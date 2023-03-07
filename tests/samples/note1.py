# Databricks notebook source
# MAGIC %md
# MAGIC # sample notebook
# MAGIC This is a sample notebook
# COMMAND ----------

# main imports
from local_databricks.ldbutils import notebook
# from local_databricks.session import SPARK

# COMMAND ----------

# inputs
# all_args  = notebook.get_notebook_params()
# foo1 = all_args.get("foo1")
# foo2 = all_args.get("foo2") 

# Get the secrets

username = notebook.get_secret(scope = "some_scope", key = "username")
password = notebook.get_secret(scope = "some_scope", key = "password")
args = {"username": username, "password": password, "foo1": "bar1", "foo2": "bar2"}
notebook.run_notebook(path = "tests/samples/note2.py", timeout_seconds = 60, arguments = args)
# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Big Title
# MAGIC 
# MAGIC Some markdown latex
# MAGIC $$e^{\pi \cdot i} +1 = 0$$

# COMMAND ----------

# read databricks sql table
# table_name = "some_table"
# notebook.display(SPARK.sql(f"SELECT * FROM {table_name}"))