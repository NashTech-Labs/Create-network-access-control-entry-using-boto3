# How to create a network access control list (NACL) entry  in a NACL using boto3


## What is network access control list (NACL)?
### A network access control list (NACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.You can follow this [link](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) to know more.



-------------

## What is the NACL entry in a VPC
### Creates an entry (a rule) in a network ACL with the specified rule number. Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the ACL, we process the entries in the ACL according to the rule numbers, in ascending order. Each network ACL has a set of ingress rules and a separate set of egress rules. You can follow this [link](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAclEntry.html) to know more.


--------------
### I have define the script to create the Network access control list[NACL] entry in the VPC. You just need to pass the region, rule action, rule number and NACL id at the run time and one more thing your aws credential (access and secret key) must be configure in your system then your resource will be create in the VPC. You need to follow the below commands.

**Files:** 

```
       create_entry.py
```
## Apply the script using below commands:

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command:

        python3 <create_entry.py>


