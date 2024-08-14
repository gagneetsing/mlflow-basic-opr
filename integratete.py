import dagshub

dagshub.init(repo_owner="gagneetsing", repo_name="mlflow-basic-opr", mlflow=True)

import mlflow

with mlflow.start_run():
    mlflow.log_param("parameter name", "value")
    mlflow.log_metric("metric name", 1)
