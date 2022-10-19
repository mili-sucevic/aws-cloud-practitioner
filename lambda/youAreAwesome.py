# A Cloud Guru: Create a Lambda Function Using the AWS Management Console 
import json

def lambda_handler(event, context):
    message = 'Hello {} {}! Keep being awesome!'.format(event['first_name'], event['last_name'])  

    #print to CloudWatch logs
    print(message)

    return {
        'message' : message
    }  

  
# Create a Test Event and Execute Lambda
{ "first_name": "Your First Name Here", "last_name": "Your Last Name Here" }
