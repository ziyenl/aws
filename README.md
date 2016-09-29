# AWS
AWS Playground Experiment

Files | Description
--- | ---
food/scrape.py | extracts images from foodnetwork.co.uk for a given ingredient type and store them in S3 Bucket. This uses BeautifulSoup, boto3 and python. 

## food/scrape.py

To use, just install boto3 and BeautifulSoup on EC2 agent. Subsequently, schedule for scrape.py to run with the specify ingredient. 



### Further Suggested Modifications
1. Scrape multiple pages of a given ingredient
2. Run a set of ingredients from a static list/possibly in dynamo db
3. Setup to run against other websites (not just foodnetwork)

I subsequently would like to have a collection of recipes and possibly store them in Dynamo DB as a json format. 

Everything conducted here is just experimentation. All images are not kept for long term storage as to ensue any copyrights issue.
