import pyspark
from local_databricks import SETTINGS
# from local_databricks.session import SPARK


def run_notebook(path:str, timeout_seconds:int, arguments:dict):
  if SETTINGS.DATABRICKS:
    pyspark.dbutils.notebook.run(path, timeout_seconds, arguments=arguments)
  else:
    # run local notebook
    pass

def get_secret(key:str, scope:str):
  if SETTINGS.DATABRICKS:
    return pyspark.dbutils.secrets.get(scope = scope, key = key)
  else:
    #get local secret
    pass

def set_enviroment(SPARK : pyspark.sql.SparkSession, key:str, value:str):
  if SETTINGS.DATABRICKS:
    SPARK.conf.set(key, value)
  else:
    #set local enviroment
    pass

def read_enviroment(SPARK: pyspark.sql.SparkSession, key:str):
  if SETTINGS.DATABRICKS:
    return SPARK.conf.get(key)
  else:
    #get local enviroment
    pass

def get_notebook_params():
  if SETTINGS.DATABRICKS:
    return dict(pyspark.dbutils.notebook.entry_point.getCurrentBindings())
  else:
    #get local notebook params
    pass