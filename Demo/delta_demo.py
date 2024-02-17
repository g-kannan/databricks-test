# Databricks notebook source
dbutils.fs.ls("/databricks-datasets/songs/data-001/")

# COMMAND ----------

df = spark.read.csv("/databricks-datasets/songs/data-001/")

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta").saveAsTable("songs")

# COMMAND ----------

# MAGIC %run ./SP-ADLS

# COMMAND ----------

df.write.format("delta").option('path','abfss://databricks-trial-demo@sadataengci.dfs.core.windows.net/TEST-ADLS/songs-tbl/').saveAsTable("songs")

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table default.songs

# COMMAND ----------

# MAGIC %sql
# MAGIC desc extended default.songsext

# COMMAND ----------

# MAGIC %sql
# MAGIC create table songsext location'abfss://databricks-trial-demo@sadataengci.dfs.core.windows.net/TEST-ADLS/songs-tbl'

# COMMAND ----------

dbutils.fs.ls("dbfs:/user/hive/warehouse/")

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from songs where `_c0` like '%ARTOOI21187B9922AA%'
