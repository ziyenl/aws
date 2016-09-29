# AWS
AWS Playground Experiment

Project | Files | Description
---|--- | ---
Scraping Food Website with S3 | food/scrape.py | extracts images from foodnetwork.co.uk for a given ingredient type and store them in S3 Bucket. This uses BeautifulSoup, boto3 and python. 

## Scraping Food Website with S3

To use, just install boto3 and BeautifulSoup on EC2 instance with IAM Role to S3. Subsequently, schedule for scrape.py to run with the specify ingredient. 
![alt text](https://github.com/ziyenl/aws/blob/master/ingredient.png "Ingredient")

### Further Suggested Modifications to food/scrape.py
1. Scrape multiple pages of a given ingredient
2. Run a set of ingredients from a static list/possibly in dynamo db
3. Setup to run against other websites (not just foodnetwork)

I subsequently would like to have a collection of recipes and possibly store them in Dynamo DB in json format. Everything conducted here is just experimentation. All images are not kept for long term storage as to ensue any copyrights issue.

### Results
