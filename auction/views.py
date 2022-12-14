from django.shortcuts import render,HttpResponseRedirect
from auction.froms import AuctionFrom,AuctionFromUser
from auction.models import Auction
from django.contrib import messages
from rest_framework import viewsets
from auction.serializers import AuctionSerializer
# Create your views here.


class Api(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer



def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            if request.method =='POST':
                fm = AuctionFrom(request.POST)
                if fm.is_valid():
                    fm.save()
                    messages.success(request,'Auction created successfully..!')
                return render(request,'auction.html',{'form':fm})
                
            else:
                fm = AuctionFrom()
                return render(request,'auction.html',{'form':fm})
        else:
            return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/login/')

def auction_del(request):
    if request.user.is_authenticated:
        auct = Auction.objects.all()
        return render(request,'aution_del.html',{'data':auct})
    else:
        return HttpResponseRedirect('/login/')

def auct_del(request,pk):
    if request.user.is_authenticated:
        auct = Auction.objects.get(id=pk)
        auct.bider_user=f'{request.user}'
        auct.save()
        if request.method == 'POST':
            u_price = request.POST.get('auction_running_price')
            o_price = auct.auction_running_price
            print("+++++++++++++++++++++++++++")
            print(auct.bider_user)
            print("+++++++++++++++++++++++++++")
            fm = AuctionFromUser(request.POST,instance=auct)
            if o_price>int(u_price):
                messages.error(request,'amount is less then curent price ')
                return render(request,'aut_del.html',{'form':fm,'data':auct})
            if fm.is_valid():
                fm.initial= {"bider_user":request.POST[auct.bider_user]}
                fm.save()
                messages.success(request,'biding successfully ')
                return render(request,'aut_del.html',{'form':fm,'data':auct})
        else:
            fm = AuctionFromUser()
            return render(request,'aut_del.html',{'form':fm,'data':auct,'name':request.user})
    else:
        return HttpResponseRedirect('/login/')