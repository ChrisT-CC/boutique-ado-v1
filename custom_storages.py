'''
Tell django that in production we want to use s3 to store our static files
whenever someone runs collectstatic and that we want any uploaded product
images to go there also
'''
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    '''
    Custom class helps to store static files in a location from the settings
    '''
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    '''
    Custom class helps to store media files in a location from the settings
    '''
    location = settings.MEDIAFILES_LOCATION
