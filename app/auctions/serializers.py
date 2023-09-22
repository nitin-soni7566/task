from rest_framework import serializers
from auctions.models import Auction

class AuctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auction
        fields = ['id','auction_name','auction_image','auction_desc','auction_price','auction_running_price','auction_startDate','auction_endDate','bider_email','bider_user_name']