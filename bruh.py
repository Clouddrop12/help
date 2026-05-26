import boto3 
import os
APIKEY = 'bedrock-api-key-YmVkcm9jay5hbWF6b25hd3MuY29tLz9BY3Rpb249Q2FsbFdpdGhCZWFyZXJUb2tlbiZYLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFTSUFTV0VMWEJEVkY3NEpGSFFEJTJGMjAyNjA1MjYlMkZ1cy1lYXN0LTElMkZiZWRyb2NrJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MjZUMTI0OTQ1WiZYLUFtei1FeHBpcmVzPTQzMjAwJlgtQW16LVNlY3VyaXR5LVRva2VuPUlRb0piM0pwWjJsdVgyVmpFTFglMkYlMkYlMkYlMkYlMkYlMkYlMkYlMkYlMkYlMkZ3RWFDWFZ6TFdWaGMzUXRNU0pITUVVQ0lDdU0wMkM3c0UlMkZwNm83ZjFOJTJGJTJCUTVHNFNTczNPWmVqcHNQcHVXVUJoRElmQWlFQWo3VkhRT3lCQkJuTklKakZvblRuREdCalk4TTRsMFBpVWpCc0dxRUk1RThxdkFNSWZoQUNHZ3d4T0RRNU56WTJNRGMwTmpZaURMSiUyQkVWUEhGazBobFNuUWVpcVpBNVE4NXIlMkJSdm5FTVUwV0F5RFk1VjExdWg5Qms5UHcwY29RSDJlaiUyQlNEM3dqb3l3YjdWd0VQMHNXcUJicUlsRzVtaENBJTJGeHJ5ZHBTJTJCRW1YR0dBcGEyRnYwMTlISm5KbDdZU1RrR0tDMlJSQXgwUGN3MkFHJTJGaFJkWXA0T3JHeHdqdTR2JTJCYyUyRlVYaDczWjA1NnZrWllqRWhFVkF6TEljRERaQkEyWktCWVpLN3pLWVBVUU4lMkJLcjljQjdqb1FqbVFmdjZsY0NvUWd6Zm9JJTJCVzkwaE9OOHMzekhFRkpta0tqamJlTnBKdWk5QiUyRldFSUh1eFZ3NEs3ZWJvaE8lMkY3S1I5WkN6V2huSmtoZWJZb0lac05KQllmNWwlMkYlMkJKOTM5d1ByJTJGY1prZllvQnRRZVdocWJrM05qOVhGVWZHJTJCTFBPc2JXRFZJWXBkNWZ6MVNsb05Id3pOOVpCaUZic25NamklMkZrZHBocldQbDJPUW1MRFJJWEhwaDFXTWRLUDRRQ0pMYTJqZ1VQSiUyRjJkT3U2d0Z2Q0VzcGVMWkhHQk9ZVDB3RWg1bXlzWHU2dW9JRUNNWWtObFB0TlA3SWlpJTJCU0V1N0h3WVQ4UGVaSzRHeEVMWFJ4cGNOcjFNZ0xCVkI2MDFHUllsUWVyU0lpSkVKOU5iaU9mek9NQnIlMkI4b3djRWhCZzI0d2htenpNanhLUHRmWnRsOVA4VXhQcmozZDh0ZWwzWUZtek5UMmd3NEt6VzBBWTYzZ0l6MjAyWWp4MTdzJTJGRzdOeUxHN04lMkJIdEVEJTJCJTJCY01qdjZSN3EydXlTcko3MWpvNFdocGhVcGNkYUtlUjMzaVJHJTJCdTEzUUFpN2w1Vk5QVnFhanc1R3NGYkEzRGN3akgxNXREbjlpcXNNTHZsMDVJaHU1dmpBdE9JVFdNOEg5Zk1DWkd4cnRmYVNFeFNReXB5TjhMeGVlUFdvVlN0Sk5oJTJGSHhOMG9PdkZ0VlFCbmcwOFV3NlZ2VXFSSEI3cTZKM3Q1TDFLbUszWGVnTW90aWZKMzdWM3ExbW5lNEtnVjk0dkR2WE1LNTJIdWVLbEJJbjBDcW41S0h4REFKMThCZk5sd1glMkI2TTB2V0pjblp1JTJCJTJGZ28zM2psZG5zdU9OSE9DVTR5UkZoN1U1UGU0TXRhTzRLNUcybyUyRlJyblB1M0VzUW13UlJmVVV5OXo5cUFGMTZxcUNoUnNYYnBlM3Y1VCUyQktIYllXcTRrWENHaHh0Sk5BZmNUUVhEdk9oVFJubUozJTJGc1B3M2VYTjFHdHpDUmFKMDBSMDNCNk01YUhKalhGazF5TmY2cXllWUdKUm1JbyUyQkF2d25QRDhpbXJBaEFKTzBFZ3EzZ0Jka1lLSzJmT2tTZFBpMUVZTE1RJTNEJTNEJlgtQW16LVNpZ25hdHVyZT05ZWViMGJiMjExZTkwZGY0OWI0Yzc2MzA5NTRhMzA3OTA5MjkxZWM1N2JjOTgwMjRiYjc3M2M5ZWY1OWU0NTZlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZWZXJzaW9uPTE='
from cmu_graphics import *
#ui (web guys lock in!!)
#code goes in here
def redrawAll(app):
    drawRect(50,50,50,50)

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
            clean_name = os.path.splitext(filename)[0].replace(" ", "_")
            clean_name = "".join(c for c in clean_name if c.isalnum() or c == "_")
            #all data is added to the the allData list
            allData.append({
                "document": {
                    "format": "pdf",
                    "name": clean_name[:20],  
                    "source": {"bytes": doc_bytes}
                        }
                    })
#the request is added to the list because claude formatting is weird 
allData.append({"text": "What are all these files trying to do? what are some common themes or goals?"})
print("Sending all "+ str(len(allData) - 1) +" documents to Bedrock")
#sends the allData list to claude and sets its response to a variable
response = client.converse( 
    modelId="us.anthropic.claude-haiku-4-5-20251001-v1:0", 
    messages=[{ 
        "role": "user", 
        "content": allData
}] 
) 
#response is set to summary variable and is printed
summary = response["output"]["message"]["content"][0]["text"]
print(summary)

runApp(width=400, height=400)