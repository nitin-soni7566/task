from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from auction.froms import AuctionFrom,AuctionFromUser,WinnerForm
from auction.models import Auction,Winner
from django.contrib import messages
from rest_framework import viewsets
from auction.serializers import AuctionSerializer
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


class Api(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer



def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            if request.method =='POST':
                fm = AuctionFrom(request.POST,request.FILES)
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
        tnow = timezone.now()
        if tnow >= auct.auction_endDate:   # for cheak auction date is expire or not 
            messages.error(request,f"{auct.auction_name} auction is sold out please bid other auction ")
            return redirect('allauctions')
        else:    
            auct.bider_email=f'{request.user.email}'
            auct.bider_user_name=f'{request.user}'
            if request.method == 'POST':
                u_price = request.POST.get('auction_running_price')
                o_price = auct.auction_running_price
                print(u_price)
                fm = AuctionFromUser(request.POST,instance=auct)
                if u_price :
                    if o_price>int(u_price):
                        messages.error(request,'amount is less then curent price ')
                        return render(request,'aut_del.html',{'form':fm,'data':auct})
                else:
                    return render(request,'aut_del.html',{'form':fm,'data':auct})
                if fm.is_valid():
                    fm.initial= {"bider_user":u_price}
                    auct.save()
                    fm.save()
                    messages.success(request,'biding successfully ')
                    return render(request,'aut_del.html',{'form':fm,'data':auct})
            else:
                fm = AuctionFromUser()
                return render(request,'aut_del.html',{'form':fm,'data':auct,'name':request.user})
    else:
        return HttpResponseRedirect('/login/')




from django.forms.models import model_to_dict
def queryset_to_list(qs,fields=None, exclude=None):
    return [model_to_dict(x,fields,exclude) for x in qs]

def winner(request):
    cheak = Winner.objects.all()
    wins = Auction.objects.all()
    ne = queryset_to_list(wins)
    t1 = timezone.now()
    for i in ne:
        if t1 >= i['auction_endDate']:

            if i['auction_name'] in cheak:
                pass
            else:
                print("data saving.............")
                win = Winner(auction=i['auction_name'],
                winner_name=i['bider_user_name'],
                email=i['bider_email'],
                winning_price=i['auction_running_price'],
                winning_date=i['auction_endDate'])

                win.save()
                print("data saved")

                send_mail(
                    'auction',
                    f"congratulations you win {i['auction_name']} you have to pay {i['auction_running_price']} rs to make yours",
                    settings.EMAIL_HOST_USER,
                    [f"{i['bider_email']}"],
                    fail_silently=False,

                )

    return HttpResponse('<h1>Hello bro</h1>')