import json


def soma(event, context):
    
    #print("context", context)
    a = event["queryStringParameters"]["a"]
    b = event["queryStringParameters"]["b"]

    #queryStringParameters = event["queryStringParameters"]
    resultado = int(a)+ int(b)

    body = {
        "resultado": resultado
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
        
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
