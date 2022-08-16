# Databricks notebook source
display(spark.range(1000))

# COMMAND ----------

dbutils.jobs.taskValues.set(key   = "is_successful", value = True)
dbutils.jobs.taskValues.set(key   = "error_code", value = "3201: Incorrect date format")
