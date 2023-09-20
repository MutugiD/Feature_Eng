
## Project Goal - Experimental   
Create end to end time series feature validation.  
Will plug in BTCUSDT price+price_features from Binance for feature importance.     
Use this for experimental iteration.    
Build on MFLow Pipeline.
Deploy on AWS EC2 with GitHUb Actions. 

Then use XGBoost/LSTM for forward looking price (for 15-30 minutes).  
Add a live data feed vs the forecasted dashboard. 

## dagshub tracking
MLFLOW_TRACKING_URI=https://dagshub.com/dennismutugi/Feature_Eng.mlflow \
MLFLOW_TRACKING_USERNAME=dennismutugi \
MLFLOW_TRACKING_PASSWORD= XXXXXXXXXXXXXXXXXXXX \
python script.py  

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/MutugiD/Feature_Eng
```
### STEP 01- Create a conda environment after opening the repository

```bash
pip install virtualenv
python -m venv features  
```

```bash
features\Scripts\activate
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/dennismutugi/Feature_Eng.mlflow \
MLFLOW_TRACKING_USERNAME=dennismutugi \
MLFLOW_TRACKING_PASSWORD=XXXXXXXXXXXXXXX \
python script.py

Run this to export as env variables:

```bash
Ubunut-based
export MLFLOW_TRACKING_URI=https://dagshub.com/dennismutugi/Feature_Eng.mlflow
export MLFLOW_TRACKING_USERNAME=dennismutugi
export MLFLOW_TRACKING_PASSWORD=XXXXXXXXXXXXXXXXXXXX

Windows-based:
set MLFLOW_TRACKING_URI=https://dagshub.com/dennismutugi/Feature_Eng.mlflow
set MLFLOW_TRACKING_USERNAME=dennismutugi
set MLFLOW_TRACKING_PASSWORD=XXXXXXXXXXXXXXXXXXXXXXX

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
    - Save the URI:	897569202249.dkr.ecr.ap-northeast-2.amazonaws.com/ml_runner

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one
## Activate inactive runner (In Ubuntu)  
Under active runners, should be marked inactive, after shutting down a EC2. 
access via SSH, then CD to the root DIR  
>>> ~/actions-runner$ ./run.sh

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = ap-northeast-2

    AWS_ECR_LOGIN_URI = 897569202249.dkr.ecr.ap-northeast-2.amazonaws.com/ml_runner

    ECR_REPOSITORY_NAME = ml_runner




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


