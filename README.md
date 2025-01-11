#Using MLflow with Google Colab

#What is MLflow?
##MLflow is an open-source platform designed to manage the end-to-end machine learning lifecycle. It provides tools for experiment tracking, model management, and deployment. The four main components of MLflow are:
•	MLflow Tracking: Log and query experiments.
•	MLflow Projects: Package data science code in a reusable and reproducible format.
•	MLflow Models: Manage and deploy models from various ML libraries.
•	MLflow Registry: Centralized model store to collaboratively manage an MLflow model.
##Using MLflow to Track Experiments
1.	Run Experiments: Execute your machine learning experiments in Colab while MLflow logs the details.
2.	Monitor Results: Use the MLflow UI to monitor and compare the results of different runs.
3.	Model Management: Manage and deploy your models using MLflow's model registry and deployment tools.

##There are steps that we should do to achieve our goal with mlflow to track experiments and make comparison between the models then register the best one after that make it challenger to challenge the champion model which is deployed:

 	First we should finish the required project from reading it to preprocessing and make EDA and fill missing and train models and make hyper tuning on cloud with google colab then we should connect with mlflow project which is run locally so the second step is …………
 	Run the mlflow project which is python project with specific libraries on specific port like this:
mlflow server --host 127.0.0.1 --port 5000

 	Third step is to make ngrok account on the official website then download the agent on your local machine and run it with these steps:
- download ngrok.exe 
- add auth token like this:
  ngrok config add-authtoken your-token
- deploy your app online:
 ngrok http http://localhost:5000
or ngrok http 5000
##Here we use also localtunnel with npm for that:
npm install –g localtunnel
Then we run it with this:
lt --port 5000 --local-host localhost
##another way:
ssh -R 80:localhost:5000 serveo.net
##Explanation why we use ngrok
Ngrok is used in Colab to create a secure tunnel from a public endpoint (internet) to a local machine (your laptop). This allows Colab to communicate with services running on your local machine. When working with MLflow, ngrok enables Colab to access your local MLflow tracking server or project running on your laptop. Here's why and how we use it:
##Why Use Ngrok?
1.	Access Local Resources: Colab runs on remote servers in the cloud, so it cannot directly access services running on your local machine. Ngrok creates a tunnel that exposes your local MLflow server to the internet, allowing Colab to interact with it.
2.	Secure Connection: Ngrok provides a secure and encrypted connection, ensuring that data transmitted between Colab and your local machine is protected.
3.	Ease of Use: Setting up ngrok is straightforward and doesn't require complex network configurations.
Finally we should use mlflow code from library in colab to send logs to our local mlflow project
