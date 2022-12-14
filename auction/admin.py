from django.contrib import admin
from auction.models import Auction
# Register your models here.
@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id','auction_name','auction_image','auction_desc','auction_price','auction_running_price','auction_startDate','auction_endDate','bider_user']