# import json

# print('Loading Function...')

# def lambda_handler(event, context):
#     # Parse out query string
#     transactionId = event['queryStringParameters']['transactionId']
#     transactionType = event['queryStringParameters']['type']
#     transactionAmount = event['queryStringParameters']['amount']

#     print('transactionId=' + transactionId)
#     print('transactionType=' + transactionType)
#     print('transactionAmount=' + transactionAmount)


#     #2 Construct the body of the response object
#     transactionResponse = {}
#     transactionResponse['transactionId'] = transactionId
#     transactionResponse['amount'] = transactionAmount
#     transactionResponse['message'] = 'Hello from Lambda land'

#     #3 Construct http response object
#     responseObject = {
#         "isBase64Encoded": False,
#         "statusCode": 200,
#         "body": json.dumps(transactionResponse),
#         "headers": {
#             "Content-Type": "application/json",
#             "Access-Control-Allow-Headers": "*",
#             "Access-Control-Allow-Origin": "*",
#             "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
#         },
#     }

#     #Return the response
#     return responseObject

import json

def lambda_handler(event, context):

    #1 - Log the event
    print('***** The event is: *****')
    print(event)

    #2 - See if the token's valid
    auth = 'Deny'
    if event['authorizationToken'] == 'Guyver1':
        auth = 'Allow'
    else:
        auth = 'Deny'

    #3 - Consturct and return the response
    authResponse = {
                "principalId": "Guyver1",
                "policyDocument": 
                    {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Action": "execute-api:Invoke",
                                "Resource": ["arn:aws:execute-api:us-east-1:396332213506:53j8tla7cg/*/*"],
                                "Effect": auth
                            },
                            
                        ]
                    }
                
                }
                

    return authResponse