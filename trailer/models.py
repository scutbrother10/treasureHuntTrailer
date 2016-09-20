from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Video(models.Model):
    # product_info_id = models.ForeignKey(Product_Info, related_name='product')
    video_name = models.CharField(max_length = 20)
    video_director = models.CharField(max_length = 40)
    video_actor = models.CharField(max_length = 40)
    video_language = models.CharField(max_length = 15)
    video_district = models.CharField(max_length = 15)
    video_tag = models.CharField(max_length = 50)
    video_type = models.CharField(max_length = 20)
    video_path = models.CharField(max_length = 60)
    video_pic_path = models.CharField(max_length = 60)
    modified_date = models.DateTimeField(auto_now_add = True)