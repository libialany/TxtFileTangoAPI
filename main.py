from dotenv import load_dotenv
load_dotenv()
import os
import boto3
from botocore.client import Config
from fastapi import FastAPI, UploadFile, File, HTTPException
from botocore.exceptions import NoCredentialsError,ClientError

s3=boto3.resource(os.getenv("RESOURCE_TYPE"), 
    endpoint_url=os.getenv("HOST_BUCKET"),
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
    aws_session_token=None,
    config=boto3.session.Config(signature_version=os.getenv("SIGNATURE_VERSION")),
    verify=False
)

bucket = s3.Bucket(os.getenv("MINIO_BUCKET_NAME"))
app = FastAPI()
@app.post("/upload/")
async def upload_file(file: UploadFile):
    try:
        with file.file as f:
            bucket.upload_fileobj(f,file.filename)
        return {"message": "File uploaded successfully"}
    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="MINIO credentials not available")
@app.get("/download/{file_name}")
async def download_file(file_name: str):
    try:
        bucket.download_file(file_name, f'{file_name}.txt')
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))
