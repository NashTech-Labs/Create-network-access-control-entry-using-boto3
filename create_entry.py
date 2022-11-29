import boto3
import time
import logging
from botocore.exceptions import ClientError


# Taking input from the user for the region

REGION= input("Please, Enter the region name where you want to Delete this NACL:-")

# setup the logger configuration
logger_info = logging.getLogger()

logging.basicConfig(level=logging.INFO,format='%(message)s')

vpc = boto3.client("ec2", region_name=REGION)

# function to create the NACL entry
def create_entry(cidr,id, from_port, to_port, protocol,action,rule_no):

    try:
        response = vpc.create_network_acl_entry(CidrBlock=cidr,Egress=False,NetworkAclId=id,PortRange={'From': from_port,'To': to_port,},
                                                                                                        Protocol=protocol,
                                                                                                        RuleAction=action,
                                                                                                        RuleNumber=rule_no)

    except ClientError:

        logger_info.exception('Sorry, Not able to create the network ACL in given VPC')
        raise
    else:
        return response


if __name__ == '__main__':

    CIDR = '0.0.0.0/0'

    # For taking the NACL ID from the user
    NACL_ID = input("Enter the NACL ID to create a NACL entry:- ")

    # taking port  from user
    FROM_PORT = int(input("Enter the port:- ")) #22

    # taking port  from user
    TO_PORT = int(input("Enter the port:- ")) #22

    # taking for the port
    PROTOCOL = input("Enter the Protocol Number like for TCP=6 :- ") #6 

    # taking the rule action from the user
    RULE_ACTION = input("Enter the rule action for the NACL entry:-  ") #allow

    # Taking the rule number from user which defined while creating    
    RULE_NUMBER = int(input("Enter the rule number for the NACL entry:-  ")) #101

    for i in range(2):
        logger_info.info('Please wait ......  \nWe are creating your NACL...\U0001F570')
        time.sleep(2)
    print("We are creating your NACL...\U0001F570")
    time.sleep(2)

    network_acl = create_entry(CIDR, NACL_ID, FROM_PORT,TO_PORT, PROTOCOL, RULE_ACTION,RULE_NUMBER)

    logger_info.info('Hurry, Your NACL Entry has been created  \U0001F44D')