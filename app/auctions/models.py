from django.db import models

class Auction(models.Model):
    auction_name = models.CharField(max_length=100)
    auction_image = models.ImageField(upload_to= 'images',max_length=500,blank=True)
    auction_desc = models.CharField(max_length=200)
    auction_price = models.PositiveIntegerField()
    auction_running_price = models.PositiveIntegerField()
    auction_startDate = models.DateTimeField(auto_now=False)
    auction_endDate = models.DateTimeField(auto_now=False)
    bider_email = models.CharField(blank=True,max_length=100)
    bider_user_name = models.CharField(blank=True,max_length=100)

    def __str__(self):
        return self.auction_name


class Winner(models.Model):
    auction = models.CharField(default='',max_length=100)
    auction_image = models.ImageField(upload_to= 'images',max_length=500,blank=True)
    winner_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    winning_price = models.PositiveIntegerField()
    winning_date = models.DateTimeField(auto_now=False)
    payment = models.BooleanField(default=False)
   
    def __str__(self):

        return self.winner_name



