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
all_args  = notebook.get_notebook_params()
foo1 = all_args.get("foo1")
foo2 = all_args.get("foo2") 
print(foo1)
print(foo2)
print(all_args)