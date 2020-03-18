from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization

# mysql operator
from airflow.operators.mysql_operator import MySqlOperator

# generic transfer
from airflow.operators.generic_transfer import GenericTransfer

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['koya.harayama@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag = DAG(
    'transfer_mysql',
    default_args=default_args,
    description='A simple mysql operation',
    schedule_interval=timedelta(days=1),
)

# t1
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# sql for t2
sql = """
with w1 as (
  select
    id
    , name
  from
    mydb1.sample
)

, w2 as (
  select
    id
    , name
  from
    mydb1.sample2
)

select
  id
  , name
from
  (
  select
    id
    , name
  from
    w1
  union all
  select
    id
    , name
  from
    w2
  ) w3
"""
t2 = GenericTransfer(
    task_id='test_m2m',
    source_conn_id='database-1-aws',
    destination_conn_id='database-2-aws',
    destination_table="mydb2.sample",
    sql=sql,
    dag=dag
)

t1 >> t2
