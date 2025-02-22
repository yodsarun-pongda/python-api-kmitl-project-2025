

# python-api-kmitl-project-2025

### Prerequisite
- Docker
- Python ^3.8
- Google CLI (https://cloud.google.com/sdk/docs/install)
  - Download zip and extract and ```./install.sh```

### The Structure
- Environment 
  - Dockerfile
- Application

### Test application
```shell
pip install -r requirements.txt
```


Starting up your application
```
uvicorn main:app --reload
```

### Deploy your application
- Login Google Cloud Platform to your project
    ```gcloud auth login```
  - Set cloud project by project Id
    ```gcloud config set project```
  - Start GCP service with 2 commands
    - ```gcloud services enable run.googleapis.com```
    - ```gcloud services enable cloudbuild.googleapis.com```
    - ```gcloud services enable iam.googleapis.com```
  - Add Permission to your project_ID
    ```
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="user:[YOUR_EMAIL]" \
    --role="roles/editor"
    ```
 
- Deploy application to Cloud Run
- Build Docker Image
  - ```gcloud auth configure-docker```
- Push Docker Image ไปที่ Google Container Registry (GCR)
  - ```gcloud builds submit --tag gcr.io/[PROJECT_ID]/tutorial-app```
- Deploy application  
```
gcloud run deploy tutorial-app \
  --image gcr.io/[PROJECT_ID]/tutorial-app \
  --platform managed \
  --region asia-southeast1 \
  --allow-unauthenticated
``` 



### Delete your application
 - ```gcloud run services delete tutorial-app```

### Clear image in local machine
```docker system prune -a```


### ตรวจสอบว่ามีค่าใช้จ่ายหรือไม่
```gcloud billing accounts list```