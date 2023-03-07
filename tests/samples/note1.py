# Databricks notebook source
# MAGIC %md
# MAGIC # sample notebook
# MAGIC This is a sample notebook
# COMMAND ----------

# main imports
from local_databricks.ldbutils import notebook
from local_databricks.session import SPARK

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
emp = [(1,"Smith",-1,"2018","10","M",3000), \
    (2,"Rose",1,"2010","20","M",4000), \
    (3,"Williams",1,"2010","10","M",1000), \
    (4,"Jones",2,"2005","10","F",2000), \
    (5,"Brown",2,"2010","40","",-1), \
      (6,"Brown",2,"2010","50","",-1) \
  ]
empColumns = ["emp_id","name","superior_emp_id","year_joined", \
       "emp_dept_id","gender","salary"]

empDF = SPARK.createDataFrame(data=emp, schema = empColumns)
empDF.printSchema()
empDF.show(truncate=False)

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40) \
  ]
deptColumns = ["dept_name","dept_id"]
deptDF = SPARK.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

# COMMAND ----------

# join some tables
notebook.display(empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"fullouter"))