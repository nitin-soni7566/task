from django import forms

from auctions.models import Auction,Winner

class AuctionFrom(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['id','auction_name','auction_image','auction_desc','auction_price','auction_running_price','auction_startDate','auction_endDate']

        widgets = {
        'auction_startDate': forms.DateTimeInput(format=('%m/%d/%Y %H:%M'), attrs={'placeholder':'Select a date', 'type':'date'}),
        'auction_endDate': forms.DateTimeInput(format=('%m/%d/%Y %H:%M'), attrs={'placeholder':'Select a date', 'type':'date'}),
        }

        # def __init__(self, *args, **kwargs):
        #     super(AuctionFrom, self).__init__(*args, **kwargs)
        #     for visible in self.visible_fields():
        #         visible.field.widget.attrs['class'] = 'form-control'

class AuctionFromUser(forms.ModelForm):
    auction_running_price= forms.IntegerField(widget= forms.NumberInput
                           (attrs={'class':'form-control'}))
    class Meta:
        model = Auction
        fields = ['auction_running_price']
        labels = {'auction_running_price':'Bid price'}

class WinnerForm(forms.ModelForm):
    class Meta:
        model = Winner
        fields = ['auction','winner_name','winning_date','email','winning_price']


 