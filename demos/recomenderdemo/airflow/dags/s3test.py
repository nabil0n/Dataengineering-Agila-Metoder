from airflow import DAG
from airflow.io.path import ObjectStoragePath
from pendulum import datetime
from airflow.decorators import task

with DAG(
    dag_id="s3test",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["ObjectStore"],
    doc_md=__doc__
):

    @task
    def list_bucket():
        """
        This task lists the contents of the bucket
        """
        base = ObjectStoragePath("s3://my-bucket/", conn_id="s3")
        directories = [ob for ob in base.iterdir() if ob.is_dir()]
        files = [f for d in directories for f in d.iterdir() if f.is_file()]
        print(files)
    
    list_bucket()