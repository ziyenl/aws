__author__ = 'ziyenl'

import boto3
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup as bs
import urllib


def clean_attribute_names(name):
    """ Clean html tags found in attribute names """
    import re
    regex = re.compile('<span .*?/span>')
    return re.sub(regex,'',name)


def get_image_attributes(soup):
    """ Get the list of Image URL from the soup. Will generalize this at some point. """
    attribute_dict = dict()
    for item in soup.body.findAll('img',{'class': 'lazy'}):
        clean_attribute_names(item.get('alt'))
        attribute_dict[clean_attribute_names(item.get('alt'))] = item.get('data-original')
    return attribute_dict


def get_soup(url):
    """ Get the soup based on given url """
    response = urllib.urlopen(url)
    return bs(response, 'html.parser')


def setup_image_bucket(name='fnpictures', location='eu-west-1'):
    """ Setup image bucket """
    s3 = boto3.resource('s3')
    try:
        s3.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint': location})
    except ClientError as _:
        pass


def save_image_to_bucket(result, bucket_name='fnpictures'):
    """ Save image to Bucket """
    s3 = boto3.resource('s3')
    for picture_name, link in result.iteritems():
        f = open(picture_name + '.jpg', 'wb')
        f.write(urllib.urlopen(link).read())
        f.close()
        s3.Object(bucket_name, picture_name).put(Body=open(picture_name + '.jpg', 'rb'))


ingredient = 'pear'
search = 'http://www.foodnetwork.co.uk/recipe/' + ingredient + '-keyword--' + ingredient + '-ingredients.html'
attributes = get_image_attributes(get_soup(search))
setup_image_bucket()
save_image_to_bucket(attributes)


