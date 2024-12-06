# 🚀 PoV Flight Simulator 🚀

Welcome to the PoV Flight Simulator

- [About](#about)
- [Getting Up and Running](#getting-up-and-running)
  - [Prerequisites](#prerequisites)
  - [Spin up all services](#spin-up-all-services)
  - [Spin up the `airlines` service](#spin-up-the-airlines-service)
  - [Spin up the `flights` service](#spin-up-the-flights-service)

# About

This application comprises the following services:

| Name | Description | Tech | Quick Link |
| :---: | :---: | :---: | :---: |
| `airlines` | Backend service | Java Spring Boot app | http://localhost:8080/swagger-ui/index.html#/ |
| `flights` | Backend service | Python Flask app | http://localhost:5001/apidocs/ |
|||

# Getting Up and Running

## Prerequisites

- Install [Docker](https://docs.docker.com/engine/install/) on your local machine
- Clone this repo to your local machine
```
git clone https://github.com/aninamu/pov-sim.git
```

## Spin up all services

From the project root, run all the services with the following command:
```
make up
```

- *The `airlines` service will run on http://localhost:8080/ with Swagger doc UI at http://localhost:8080/swagger-ui/index.html#/*
- *The `flights` service will run on http://localhost:5001/ with Swagger doc UI at http://localhost:5001/apidocs/*


Stop the services with the following command:
```
make down
```

Continue reading to see how to spin up an individual service as opposed to running all services at once.

## Spin up the `airlines` service   

From the `airlines` directory:

Build the app
```
make build
```

Run the app
```
make run
```
*The `airlines` service will run on http://localhost:8080/ with Swagger doc UI at http://localhost:8080/swagger-ui/index.html#/*

Alternatively, use a single command to both build and run the app
```
make start
```

Gracefully stop the app
```
make stop
```

Clean up the container(s)
```
make clean
```

## Spin up the `flights` service

From the `flights` directory:

Build the app
```
make build
```

Run the app
```
make run
```
*The `flights` service will run on http://localhost:5001/ with Swagger doc UI at http://localhost:5001/apidocs/*

Alternatively, use a single command to both build and run the app
```
make start
```

Gracefully stop the app
```
make stop
```

Clean up the container(s)
```
make clean
```

# TODO: Batch Requests

This repo includes a shell script in `batch_requests.sh` that allows you to make batch requests to an endpoint to generate higher volumes of traffic.

Note: You may need to run the following command to make the script executable:
```
chmod +x batch_requests.sh
```

## Usage
Running the script entails executing a shell command of this format from the base root of the repo:
```
./batch_requests.sh <endpoint> <num_requests>
```

### Example - Ping GET airlines endpoint 100 times
```
./batch_requests.sh http://localhost:3000/airlines 100
```

### Example - Trigger error on GET airlines endpoint 100 times
```
./batch_requests.sh http://localhost:3000/airlines/raise 100
```

### Example - Ping GET flights endpoint 100 times:
```
./batch_requests.sh http://localhost:3000/flights/AA 100
```

### Example - Trigger error on GET flights endpoint 100 times
```
./batch_requests.sh http://localhost:3000/flights/AA/raise 100
```

_Note: These sample commands assume the application you wish to ping is running locally at http://localhost:3000. Replace with the proper value as needed._


# Deploying a Helm chart

You may wish to deploy a Helm chart to complete one of the tasks. This repo contains an example Helm chart that can be used for a sample Kubernetes deployment.

Included is a recommended approach for using [Minikube](https://minikube.sigs.k8s.io/docs/) to deploy a local Kubernetes cluster.

## Prerequisites

- Install minikube https://minikube.sigs.k8s.io/docs/start/
- Install helm https://helm.sh/docs/intro/install/

## Getting up and running

Start your cluster
```
minikube start
```

Option to view the local Kubernetes dashboard
```
minikube dashboard
```

Install the sample Helm chart
```
helm install sample-chart helm-charts/sample-chart
```

Confirm the pod is up and running
```
kubectl get pods
```
