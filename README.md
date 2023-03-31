# Computer Vision with Tensor Flow

This project was based on Object Detection for
Smart Cities.
Due to GPU constraints, I've decided to run this models out
on Google Colab. 

# Database Generation

```sh
Database Generation
Decompress original Database
JSON File Route Generation
JSON Source & Structure
From CSV to TFRecord
```

# Training Model
```sh

Decompress the Pre-Trained Model
Pipelines set-up
Route definition
Map Label
Object Detection Model Training 
Loaded to TensorBoard

```

# Inference Model

```sh
Package & Object Detection Set-up
Model Decompression
Inference Procedure 
Labeling Process were performed at linkedai.com
the retrieved and load it to the model
Applying Object Detection

```


# Object Oriented Programs 

```sh
prediction.py, cetroidtracker.py
&
trackableobject.py were class performed following
OOP convention to support the model activity
These are also need it to perform centroid allocation on
object detection performance.
```


# App.py

```sh
Laptop or Desktop environments run way different
as it could be from server, then, app.py was set up
in order to make it run.
```

# Google Cloud Platform Dockerized 

```sh
As soon as the model is set up and run it out
then, follow the next steps to dockerize it:
docker build -t python-smartcity .
docker run python-smartcity
gcloud auth login
Get & upload the verification code
gcloud auth configure-docker
```

# Build Image
```sh
From GCP get project ID
gcloud config set project *paste the GCP project ID*
gcloud builds summit --tag gcr.io/*project-name*/python-smartcity --timout=6000s
and deploy it.
```
# Cloud Run Server 
```sh
Create Service
bring & paster Container Image
Automated Scale (instance number: 10)
Instance Minimal Number (instance number: )
port: 8000
CPU: 2
Memory 2GiB
Response Time: 3600
Conteiner by Answer: 80
Fistr Generation
& Create
```

# Base64 Platform & Postman
```sh
To translate, convert and reploid video 
Postman & Base64 were used to perform video converions
```