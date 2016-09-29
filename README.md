# AWS
AWS Playground Experiment

Files | Description
--- | ---
food/scrape.py | extracts images from foodnetwork.co.uk for a given ingredient type and store them in S3 Bucket. This uses BeautifulSoup, boto3 and python. 

## food/scrape.py

To use, just install boto3 and BeautifulSoup on EC2 agent. Subsequently, schedule for scrape.py to run with the specify ingredient. 



### Further Suggested Modifications
1. Extend it to scrape multiple pages of a given ingredient
2. Extend it to run a set of ingredients from a static list/possibly in dynamo db
3. Extend it to other websites (not just foodnetwork)

My intend subsequently is to scrape out the recipes and possibly store them in Dynamo DB as a json format. 

Everything conducted here is just experimentation. All images are not kept for long term storage as to ensue any copyrights issue.
