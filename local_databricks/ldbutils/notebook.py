
import json
import os
import sys

from local_databricks import SETTINGS, logger
from local_databricks.session import DBUTILS, DISPLAY, SPARK


def display(obj):
  if SETTINGS.DATABRICKS:
    DISPLAY(obj)
  else:
    # display local
    print(obj)

def run_notebook(path:str, timeout_seconds:int, arguments:dict):
  logger.info(f"Running python {path} with arguments {arguments}")
  if SETTINGS.DATABRICKS:
    DBUTILS.notebook.run(path, timeout_seconds, arguments=arguments)
  else:
    # run local notebook
    kwargs = json.dumps(arguments)
    os.system(f"python {path} {kwargs}")
    

def get_secret(key:str, scope:str):
  logger.info(f"Getting secret {key} from scope {scope}")
  if SETTINGS.DATABRICKS:
    return DBUTILS.secrets.get(scope = scope, key = key)
  else:
    #get local secret
    return os.environ[key] #TODO: find a better way to do this

def set_enviroment(key:str, value:str):
  logger.info(f"Setting enviroment {key} to {value}")
  if SETTINGS.DATABRICKS:
    SPARK.conf.set(key, value)
  else:
    #set local enviroment
    os.environ[key] = value

def read_enviroment(key:str):
  logger.info(f"Reading enviroment {key}")
  if SETTINGS.DATABRICKS:
    return SPARK.conf.get(key)
  else:
    #get local enviroment
    return os.environ[key]

def get_notebook_params():
  logger.info(f"Getting notebook input params")
  if SETTINGS.DATABRICKS:
    return dict(DBUTILS.notebook.entry_point.getCurrentBindings())
  else:
    #get local notebook params
    return dict(sys.argv[1])