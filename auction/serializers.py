from rest_framework import serializers
from auction.models import Auction

class AuctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auction
        fields = ['id','auction_name','auction_desc','auction_price','auction_running_price','auction_startDate','auction_endDate']