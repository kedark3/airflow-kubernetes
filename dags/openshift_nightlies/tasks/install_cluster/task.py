import json
from airflow.operators.bash_operator import BashOperator



def get_task(dag, platform, version, config):
    import logging 
    import sys

    log = logging.getLogger("airflow.task.operators")
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    log.addHandler(handler) 
    return BashOperator(
        task_id=f"install_openshift_{version}_{platform}",
        depends_on_past=False,
        bash_command=f"chmod +x /opt/airflow/dags/repo/dags/openshift_nightlies/tasks/install_cluster/scripts/install_cluster.sh; /opt/airflow/dags/repo/dags/openshift_nightlies/tasks/install_cluster/scripts/install_cluster.sh -p {platform} -v {version} -j {config}",
        retries=3,
        dag=dag,
)