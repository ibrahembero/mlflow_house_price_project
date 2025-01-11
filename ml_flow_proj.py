# we install mlflow lib or tool with: pip install mlflow
# This will install MLflow, which is an open-source platform for managing the end-to-end
# machine learning lifecycle, including experimentation, reproducibility, and deployment.
# with: mlflow ui // we can run the local version of mlflow
# mlflow server --host 127.0.0.1 --port 5000
# mlflow server --host 127.0.0.1 --port 5001
import os

local_artifact_path =r'C:\bero\shAI\تدريب قفزة\Content_Of_Course\week 6\mlflow_project_py\mlartifacts\838641042170767551\7803dcc814d14436a0810dae4053bdaa\artifacts\Random Forest_model\MLmodel'
if os.path.exists(local_artifact_path):
    print("File exists")
else:
    print("File not found")
    