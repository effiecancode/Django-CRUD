# db_token.py
import boto3

def generate_aurora_token(endpoint, region):
    client = boto3.client('dsql', region_name=region)
    token = client.generate_db_connect_admin_auth_token(endpoint, region)
    print(token)
    return token

# endpoint = "uiabtxahshv6at5pcfidcxfnbq.dsql.us-east-1.on.aws"
# region = "us-east-1"

# generate_aurora_token(endpoint, region)
