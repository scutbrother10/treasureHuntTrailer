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
    video_thumbnail_path = models.CharField(max_length = 200)
    modified_date = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
       return str(self.id) + ". " + self.video_name


class Product(models.Model):
   video = models.ForeignKey('trailer.Video', related_name='products')
   product_name = models.CharField(max_length=50)
   product_type = models.CharField(max_length=50)
   product_show_time = models.IntegerField()
   product_pic_path = models.CharField(max_length=200)
   product_buy_url = models.CharField(max_length=200)
   product_key_en = models.CharField(max_length=50)
   product_key_ch = models.CharField(max_length=50)

   def __str__(self):
       return str(self.id) + ". " + self.product_name