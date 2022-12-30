from django.contrib import admin
from auction.models import Auction,Winner
# Register your models here.

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id','auction_name','auction_image','auction_desc','auction_price','auction_running_price','auction_startDate','auction_endDate','bider_email','bider_user_name']



@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ['auction','winner_name','email','winning_price','winning_date','payment']