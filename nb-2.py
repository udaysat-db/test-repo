# Databricks notebook source
is_successful = dbutils.jobs.taskValues.get(taskKey    = "task-1", \
                            key        = "is_successful", \
                            default    = True, \
                            debugValue = True)

error_code = dbutils.jobs.taskValues.get(taskKey    = "task-1", \
                            key        = "error_code", \
                            default    = "", \
                            debugValue = "")

# COMMAND ----------

print(is_successful)
print(error_code)

# COMMAND ----------


