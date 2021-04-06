import cv2
cap = cv2.VideoCapture(0)
myphoto = "rajit.jpg"
ret , photo = cap.read()
cv2.imwrite( myphoto , photo)
cap.release()
region = "ap-south-1"
bucket = "aiawswrkshp"
myphoto = "rajit.jpg"
import boto3
upimage = "file.jpg"
s3 = boto3.resource('s3')
s3
s3.Bucket(bucket)
s3.Bucket(bucket).upload_file(myphoto , upimage)
rek = boto3.client('rekognition' , region )
response_face = rek.detect_faces(
     Image={
          'S3Object': {
              'Bucket': bucket,
              'Name': upimage,
          }
      },
    Attributes = ['ALL']
)
import os
if response_face['FaceDetails'][0]['Smile']['Value'] == False:
    os.system("rhythmbox-client --play")
    x = input("Enter p to pause:")
    if ( x == "p"):
      os.system("rhythmbox-client --pause")

