# Databricks notebook source
service_credential =dbutils.secrets.get('azkv','secretvaluedatabrickstrial')
sa = "sadataengci"

spark.conf.set(f"fs.azure.account.auth.type.{sa}.dfs.core.windows.net", "OAuth")
spark.conf.set(f"fs.azure.account.oauth.provider.type.{sa}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set(f"fs.azure.account.oauth2.client.id.{sa}.dfs.core.windows.net", "f13c0981-5250-4db9-ab92-fb114878b23e")
spark.conf.set(f"fs.azure.account.oauth2.client.secret.{sa}.dfs.core.windows.net", service_credential)
spark.conf.set(f"fs.azure.account.oauth2.client.endpoint.{sa}.dfs.core.windows.net", "https://login.microsoftonline.com/1975a593-15cd-4a2f-9794-655a0278a52e/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://databricks-trial-demo@sadataengci.dfs.core.windows.net")
