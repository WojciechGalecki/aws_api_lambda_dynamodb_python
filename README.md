# install aws cli and sam cli

# create new AWS s3 bucket:
aws --profile <profile_name> s3api create-bucket --bucket <bucket_name> --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1

# pack the project:
sam package \
   --profile <profile_name> \
   --template-file template.yaml \
   --output-template-file serverless-output.yaml \
   --s3-bucket <bucket_name>
   
# deploy:
sam deploy \
   --profile <profile_name> \
   --template-file serverless-output.yaml \
   --stack-name SHOPPINGAPP \
   --capabilities CAPABILITY_IAM