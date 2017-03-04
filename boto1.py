import boto

conn = boto.connect_s3()
bucket = conn.get_bucket('my-bucket')

for obj in bucket:
    print(obj.key, obj.last_modified)
