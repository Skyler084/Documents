spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "<your_access_key>")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "<your_secret_key>")