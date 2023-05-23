import boto3
import json

client = boto3.client("rekognition", region_name="ap-northeast-1")

with open("../cat.jpg", "rb") as f:
    image = f.read()
    resp = client.detect_labels(Image={"Bytes":image})
    print(json.dumps(resp, indent=2))
