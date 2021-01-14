#!/usr/bin/env python3

from aws_cdk import core
from s3_stack.s3 import S3Stack
from aws_cdk_exemplo.aws_cdk_exemplo_stack import AwsCdkExemploStack


app = core.App()
S3Stack(app, 'stack-cdk-bucket')
app.synth()
