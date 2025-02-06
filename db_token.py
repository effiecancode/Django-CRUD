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


# PGSSLMODE=require \
# psql --dbname postgres \
#     --username admin \
#     --host z4abtxahshtsf3garatpdmzbai.dsql.us-east-2.on.aws

# aws rds modify-db-cluster \
# >     --db-cluster-identifier uiabtxahshv6at5pcfidcxfnbq \
# >     --vpc-security-group-ids sg-0dc124aadcd8c25ba
