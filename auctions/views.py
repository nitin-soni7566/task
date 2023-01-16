from django.forms.models import model_to_dict
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from auctions.forms import AuctionFrom, AuctionFromUser, WinnerForm
from auctions.models import Auction, Winner
from django.contrib import messages
from rest_framework import viewsets
from auctions.serializers import AuctionSerializer
from django.utils import timezone
from datetime import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import BasicAuthentication

# Create your views here.


class Api(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            if request.method == 'POST':
                fm = AuctionFrom(request.POST, request.FILES)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, 'Auction added successfully..!')
                return render(request, 'auction.html', {'form': fm})
            else:
                fm = AuctionFrom()
                return render(request, 'auction.html', {'form': fm})
        else:
            return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/login/')


def auction_list(request):
    if request.user.is_authenticated:
        auct = Auction.objects.all()
        return render(request, 'auction_list.html', {'data': auct})
    else:
        return HttpResponseRedirect('/login/')


def auction_detail(request, pk):
    if request.user.is_authenticated:
        auct = Auction.objects.get(id=pk)
        tnow = timezone.now()
        if tnow >= auct.auction_endDate:   # for cheak auction date is expire or not
            messages.error(
                request, f"{auct.auction_name} auction is sold out please bid aother auction ")
            return redirect('allauctions')
        else:
            auct.bider_email = f'{request.user}'
            auct.bider_user_name = f'{request.user.name}'
            if request.method == 'POST':
                u_price = request.POST.get('auction_running_price')
                o_price = auct.auction_running_price
                print(u_price)
                fm = AuctionFromUser(request.POST, instance=auct)
                if u_price:
                    if o_price > int(u_price):
                        messages.error(
                            request, 'amount is less then curent price ')
                        return render(request, 'auction_details.html', {'form': fm, 'data': auct})
                else:
                    return render(request, 'auction_details.html', {'form': fm, 'data': auct})
                if fm.is_valid():
                    fm.initial = {"bider_user": u_price}
                    auct.save()
                    fm.save()
                    messages.success(request, 'biding successfully ')
                    return render(request, 'auction_details.html', {'form': fm, 'data': auct})
            else:
                fm = AuctionFromUser()
                return render(request, 'auction_details.html', {'form': fm, 'data': auct, 'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

# form convert query set into python list

def queryset_to_list(qs, fields=None, exclude=None):
    return [model_to_dict(x, fields, exclude) for x in qs]

def winner(request):
    win = Winner.objects.all()
    win_list = queryset_to_list(win)
    auctions = Auction.objects.all()
    auct_list = queryset_to_list(auctions)
    present_time = timezone.now()
    a_list = []
    for k in range(len(win_list)):
        a_list.append(win_list[k]['auction']) 
    print(a_list)   
    for i in auct_list:
        if present_time >= i['auction_endDate'] and i['auction_name'] not in a_list:
            print(i['auction_image'])
            print("else part") 
            win = Winner(auction=i['auction_name'],
                    auction_image=i['auction_image'],
                    winner_name=i['bider_user_name'],
                    email=i['bider_email'],
                    winning_price=i['auction_running_price'],
                    winning_date=i['auction_endDate'])
            win.save()
            subject = 'Auction Bidding'
            form = settings.EMAIL_HOST_USER
            to = f"{i['bider_email']}"
            msgs = f"""
                    <div>
                        <center> <b> <u> Congratulations...!</u>&#10024; &#10024;</b></center>
                        <div> 
                            <h3>You win auction <b style="color: red;">{i['auction_name']}</b> &#127873;</h3>
                                <ul>
                                <img src="media/{i['auction_image'].url}" alt="" width="100px" style="border-radius: 50%;"> <br> <br>
                                    <li>winning date: {i['auction_endDate']}    
                                    </li>
                                    <li>
                                        pay price: {i['auction_running_price']} rs.
                                    </li>
                                    </ul>
                                    <p>If you want to its yours you have to pay <b style="color: green;" >{i['auction_running_price']} rs.</b></p>
                                </div>
                            </div>
                        """
            mail = EmailMultiAlternatives(subject,msgs,form,[to])
            mail.content_subtype='html'
            mail.send()
            print("send mail")
    return redirect('dashbord')