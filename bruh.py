import boto3 
import os
import requests
import base64
BEDROCK_API_KEY = "bedrock-api-key-YmVkcm9jay5hbWF6b25hd3MuY29tLz9BY3Rpb249Q2FsbFdpdGhCZWFyZXJUb2tlbiZYLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFTSUFTV0VMWEJEVkFXWkFGQVZTJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZiZWRyb2NrJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMjAwNDQ0WiZYLUFtei1FeHBpcmVzPTQzMjAwJlgtQW16LVNlY3VyaXR5LVRva2VuPUlRb0piM0pwWjJsdVgyVmpFRFVhQ1hWekxXVmhjM1F0TVNKSU1FWUNJUURwUiUyRk5BRFh1ZllIQ3FZemxFMzVUMHlLVmk3RVBXaENpUGlxeWlmaiUyRmVWd0loQUxkWmZZUnN5bVE4RyUyQlNLQ3IycUZiU0xNd1NDdWZqWDRVOTlhVkFzN251QktzVURDUDMlMkYlMkYlMkYlMkYlMkYlMkYlMkYlMkYlMkYlMkZ3RVFBaG9NTVRnME9UYzJOakEzTkRZMklnekdSQTlZaWJIbTdHRXlvWElxbVFONTlWMk1HZUNkSFpuYlR6N1RmdTNrQnVoOVpnQWpLS1VHQTZsdk9ZSzh3YU9rTTBHME5QY3QlMkJuc2dDVDl6VVJxQVQyT2ZsMiUyQlVERVBFVTNKa1ZEalVuYUNzNkhwU3NFYjd2NnBBMzZQRCUyQjk2RmtSWmJUZ0QwWFBDT3IwRE81TjAzcGVHd1MxV3RzdlFsNW5FN0huRW00NXlQYkVNWHM4cDhnd1F5QTlRbVJ4aTFSSXNUOEdUbHdDV2dxN1VCMjh6SlFFNlQxZnJtJTJGdmZHaWt5RndtVkt5Yk8lMkY0NkxaVGxBTml2cFBXeXl4JTJGZm5HMVFGNUxrayUyQmVFQ1kxRHZOWGlnU1lLZDhIeEFGVWJCb1p4OWM4emU1NDBpZiUyQmtqS1pWOXd5MiUyRnk2VUJZTDRnTElKcjRVT0FlUERRYnMwblA4dU0lMkZvR2VUZGRTOXpPTyUyRklEMUpROHppZVNCeVJtRkdBSVN2dHVxVHZWTVZYcGVrTE8ycnROd1JSM0NOQXIlMkZhYnNRVHFZZW4yZEI0NmclMkJMa1hxT3RPV0FpazRUVGgwS0Q2ZkklMkIlMkJTdk9vNWc1aWpzTzg4MXBUS1NUNWM3MFpuVlNRM0I2OWhpRWVvcVFGOTkwQVl2YVBzM1hYQXJVeWZQM3NaQVI1bW9DamVzWiUyRmNTaFVpJTJCZ2s5WGYzc055eElIaGlXJTJGWnRDZ1RFWmc2QTlIRENxdnZGTDlJQndFRFVFdWFvOEZNTHVVOHRBR090MENHSWVrM3M3RkhBaERjNDJVcSUyRllpSGFpZXhLZEJ4QzdxYzZrbUVmT3ZxTlElMkZmbFg4eG9xbTY2cGFLTlBwTXRnJTJCeVpBNFIlMkZJZFRNZllpYWVES1BZZndXdHRlYUxnVnFHbGdnaEE0RSUyRjRKVVJqN2o5RkxZUlhWZG00WFdmcm1Nbk9rUG5ST2JNQkJ0QmRueEJDOCUyQkJ1cXozMGVWUXNWVDROd2lBbnRxQzdlS1BBWDFjNjNzRVl2b3p5JTJGTSUyQjJUTXZEdG9YN3FuRVhGN2UwVXZ4TmU2ZzlJM2tEVnFyZm1vS2xQRkNRSyUyRnElMkJ1Z3dQclNNJTJCQjdhcUVyOG8xVkdVMmRlSUNPJTJCRkY4ZEVSVmpNYlowbUV4ZXprMUJ4OFhoT0s1eHUlMkIlMkZxQW1UNDB6WGxqcFBrZ0hOcm9VR0dMS0s0Y3J2T2Z4d29hUWtxd0pjeiUyRjVieWgzRk8lMkZQWHgzaGJONU84dWxjWFRXZ2NKSVk3V0x5U1lBTE5FSnZXSVclMkZ1YkhQNk1WandIVUNpZzEyTmVpR1FLOW5hOU1tbGRQJTJGeEtnbk00ejlsNmNRVkNKaVR0ayUyQiUyQlNnaWtvV3A3dE8lMkZOaHhkb3FGMm1PMG5FUHAzJTJGeDNOVm1kVGclM0QlM0QmWC1BbXotU2lnbmF0dXJlPTQ5Zjg4MDI5NzRlYTNjODYxMzE1YzcwMmRmZDI4MmNlZjEyZmNlM2NiNjc0MThkMjI1MTdjMzQxMjM0YjhmZmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JlZlcnNpb249MQ=="
REGION = "us-east-1" 

# Bedrock API Key Endpoint
URL = f"https://bedrock-runtime.us-east-1.amazonaws.com/model/global.anthropic.claude-sonnet-4-5-20250929-v1:0/converse"
headers = {
    "Authorization": f"Bearer {BEDROCK_API_KEY}",
    "Content-Type": "application/json"
}
#all data list holds everything from the files read
allData=[]
#for loop cycles through and reads every file in the collegeEssay folder
for filename in os.listdir(r"C:\Users\jonno\geekathon\collegeEssays"):
    if filename.endswith('.pdf'):
        full_path = os.path.join(r"C:\Users\jonno\geekathon\collegeEssays", filename)
        if os.path.isfile(full_path):
            print("Processing: " + filename+ " into memory")
            with open(full_path, 'rb') as f:
                doc_bytes = f.read()
            # sticks and stones dont break your bones bruh
            #formats the data for claude to read (no idea how ts works)
                # Base64 encode the binary data so it can safely travel over JSON
            encoded_string = base64.b64encode(doc_bytes).decode('utf-8') 
            clean_name = os.path.splitext(filename)[0].replace(" ", "_")
            clean_name = "".join(
                c for c in clean_name if c.isalnum() or c == "_")
            #all data is added to the the allData list
            allData.append({
                "document": {
                    "format": "pdf",
                    "name": clean_name[:20],  
                    "source": {"bytes": encoded_string}
                        }
                    })
#the request is added to the list because claude formatting is weird 
allData.append({"text": "What are all these files trying to do? what are some common themes or goals?"})
print("Sending all "+ str(len(allData) - 1) +" documents to Bedrock")
#sends the allData list to claude and sets its response to a variable
response = requests.post( 
    url=URL,
    headers=headers,  # Ensure your Bearer token headers dict is defined above this
    json={"messages": [{"role": "user", "content": allData}]},
) 
#response is set to summary variable and is printed
if response.status_code == 200:
    response_dict = response.json()
    summary = response_dict["output"]["message"]["content"][0]["text"]
    print(summary)
else:
    print(f"❌ Request Failed with Status Code {response.status_code}")
    print(response.text)