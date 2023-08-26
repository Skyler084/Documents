#read the data from s3 and to see the data
spark.read.csv("s3://healthinsurancebucket01/uncleaneddata/subscriber.csv").show()

#create data frame and clean it
subscriber_df = spark.read.option("header","true").csv("s3://healthinsurancebucket01/uncleaneddata/subscriber.csv")

#fill nulls with N/a
columns_to_replace = ["first_name", "last_name","Street","Gender", "subgrp_id", "Elig_ind", "Phone","Country"]
subscriber_df = subscriber_df.fillna("N/A", subset=columns_to_replace)

#write the data to redshift tables
subscriber_df.write.format("redshift")\
    .option("url", "jdbc:redshift://default-workgroup.671359249777.us-east-1.redshift-serverless.amazonaws.com:5439/dev")\
    .option("dbtable", "ProjectOutput.subscriberdata")\
    .option("driver","com.amazon.redshift.jdbc42.Driver")\
    .option("tempdir", "s3a://healthinsurancebucket01/cleaneddata/") \
    .option("user", "<your_user>").option("password", "<your_password>") \
    .option("aws_iam_role", "arn:aws:iam::671359249777:role/redshiftAdmin") \
    .mode("overwrite").save()