Project Overview

This project demonstrates deploying a machine learning model using Docker and Kubernetes.
A hospital scheduling prediction model is trained using a real-world hospital scheduler dataset and exposed as a REST API using FastAPI, then containerized and prepared for scalable cloud deployment.

The API helps predict or assist in hospital scheduling decisions such as patient prioritization or appointment and resource allocation based on the provided input features.

Technologies Used

Python 3.10

Scikit-learn

FastAPI

Docker

Kubernetes

Dataset Description

The Hospital Scheduler Dataset contains records related to hospital operations such as patient details, appointment timing, resource usage, and scheduling constraints.
The dataset is used to train a machine learning model that supports intelligent scheduling decisions.

API Endpoints

GET /healthz – Application health check

POST /predict – Returns scheduling-related predictions based on input features

Download the Project

Clone the repository from GitHub:

git clone <REPOSITORY_URL>
cd hospital-scheduler

How to Run the Application Locally
1. Install Dependencies
pip install -r requirements.txt

2. Train the Machine Learning Model
python train_model.py


Expected output:

Mean Squared Error: ...
Model saved as model.pkl

3. Start the API
python -m uvicorn app:app --reload

4. Open in Browser

API Documentation:
http://127.0.0.1:8000/docs

Health Check:
http://127.0.0.1:8000/healthz

Run with Docker
Build Docker Image
docker build -t hospital-scheduler-api .

Run Docker Container
docker run -p 8000:8000 hospital-scheduler-api


Access the API at:

http://localhost:8000/docs

Kubernetes Deployment

Create the deployment:

kubectl create deployment hospital-scheduler-api \
--image=<dockerhub-username>/hospital-scheduler-api


Expose the service:

kubectl expose deployment hospital-scheduler-api \
--type=NodePort --port=8000


Check running resources:

kubectl get pods
kubectl get svc


After deployment, the application is accessible through the NodePort service and monitored using Kubernetes health checks.

Health Checks

Liveness Probe: Ensures the application is running correctly

Readiness Probe: Ensures the application is ready to receive traffic

Both probes are implemented using the /healthz endpoint.

Author

Mark Sherif

Ahmed Alaa

Youssef Yasser
