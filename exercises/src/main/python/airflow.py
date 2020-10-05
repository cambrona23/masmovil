from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {'owner': 'airflow',
                'dependes_on_past': False,
                'start_date': datetime(2020, 10, 5, 3, 00, 00),
                'retires': 1,
                'retry_delay': timedelta(seconds=5)
                }

test = DAG(
    'test',
    default_args=default_args,
    description='Masmovil',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(dag=test, task_id='start')
end = DummyOperator(dag=test, task_id='end')

start >> end

push_func = PythonOperator(
    task_id='push_func',
    provide_context=True,
    python_callable=values_function,
    dag=dag)
N = 7

def listaImpares(N):
    for x in range(N):
        if(x % 2 != 0):
            list.append('task' + x + ' >> ')

    return list

task1 = DummyOperator(dag=test, task_id='task1')
task2 = DummyOperator(dag=test, task_id='task2', python_callable=listaImpares)
task3 = DummyOperator(dag=test, task_id='task3')
task4 = DummyOperator(dag=test, task_id='task4',  python_callable=listaImpares)
task5 = DummyOperator(dag=test, task_id='task5')
task6 = DummyOperator(dag=test, task_id='task6',  python_callable=listaImpares)

for i in range(1, N):
    if(x % 2 != 0):
        listaImpares(N) >> 'task' + i + '>>'
    else task + 1 >>

task1 >> [task1, task3, task5] >> task2 >> task3 >> [task1, task3, task5] >> task4 >> task5 >> [task1, task3, task5] >> task6
