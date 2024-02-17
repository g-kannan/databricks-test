# Databricks notebook source
spark.conf.set("fs.azure.account.key.sadataengci.dfs.core.windows.net",
    "Test")

# COMMAND ----------

dbutils.fs.ls("abfss://databricks-trial-demo@sadataengci.dfs.core.windows.net")

# COMMAND ----------

sa = "sadataengci"
spark.conf.set(f"fs.azure.account.auth.type.{sa}.dfs.core.windows.net", "SAS")
spark.conf.set(f"fs.azure.sas.token.provider.type.{sa}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set(f"fs.azure.sas.fixed.token.{sa}.dfs.core.windows.net", "Test")
