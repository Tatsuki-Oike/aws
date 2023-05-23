import boto3
import json

client = boto3.client("translate", region_name="ap-northeast-1")

text = "ようこそ、データサイエンス研究所へ"

resp = client.translate_text(
    Text=text,
    SourceLanguageCode="ja",
    TargetLanguageCode="en"
)
print(json.dumps(resp, indent=2))
