import boto3
import json

# Initialize the IAM client
iam = boto3.client('iam')


def create_iam_user(username):
    try:
        response = iam.create_user(
            UserName=username,
            Path='/system/'
        )
        print(f"IAM user '{username}' created successfully.")
        return response['User']['UserName']
    except Exception as e:
        print(f"Error creating IAM user: {str(e)}")
        return None


def create_access_key(username):
    try:
        response = iam.create_access_key(UserName=username)
        print(f"Access key created for user '{username}'.")
        return response['AccessKey']
    except Exception as e:
        print(f"Error creating access key: {str(e)}")
        return None


def create_iam_policy(policy_name, policy_document):
    try:
        response = iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document)
        )
        print(f"IAM policy '{policy_name}' created successfully.")
        return response['Policy']['Arn']
    except Exception as e:
        print(f"Error creating IAM policy: {str(e)}")
        return None


def attach_user_policy(username, policy_arn):
    try:
        iam.attach_user_policy(
            UserName=username,
            PolicyArn=policy_arn
        )
        print(f"Policy attached to user '{username}' successfully.")
    except Exception as e:
        print(f"Error attaching policy to user: {str(e)}")


# Main execution
if __name__ == "__main__":
    # Define the IAM user and policy names
    iam_username = "terraform-user"
    policy_name = "TerraformEC2NetworkPolicy"

    # Create IAM user
    user = create_iam_user(iam_username)
    if user:
        # Create access key for the user
        access_key = create_access_key(user)
        if access_key:
            print(f"Access Key ID: {access_key['AccessKeyId']}")
            print(f"Secret Access Key: {access_key['SecretAccessKey']}")

        # Define the full policy document
        policy_document = {
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "AllowAllS3Actions",
                        "Effect": "Allow",
                        "Action": "s3:*",
                        "Resource": "*"
                    },
                    {
                        "Sid": "AllowAllDynamoDBActions",
                        "Effect": "Allow",
                        "Action": "dynamodb:*",
                        "Resource": "arn:aws:dynamodb:*:*:table/terraform-state-lock"
                    },
                    {
                        "Sid": "AllowAllEC2Actions",
                        "Effect": "Allow",
                        "Action": "ec2:*",
                        "Resource": "*"
                    },
                    {
                        "Sid": "AllowAllVPCActions",
                        "Effect": "Allow",
                        "Action": [
                            "ec2:*Vpc*",
                            "ec2:*Subnet*",
                            "ec2:*Gateway*",
                            "ec2:*Vpn*",
                            "ec2:*Route*",
                            "ec2:*Address*",
                            "ec2:*NetworkAcl*",
                            "ec2:*SecurityGroup*"
                        ],
                        "Resource": "*"
                    },
                    {
                        "Sid": "AllowRelatedServices",
                        "Effect": "Allow",
                        "Action": [
                            "elasticloadbalancing:*",
                            "autoscaling:*",
                            "cloudwatch:*",
                            "logs:*",
                            "iam:PassRole"
                        ],
                        "Resource": "*"
                    }
                ]
            }
        }

        # Create IAM policy
        policy_arn = create_iam_policy(policy_name, policy_document)
        if policy_arn:
            # Attach policy to user
            attach_user_policy(user, policy_arn)

    print("Script execution completed.")
