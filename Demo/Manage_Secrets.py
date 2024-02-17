# Databricks notebook source
dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list("azkv")

# COMMAND ----------

dbutils.secrets.help()
