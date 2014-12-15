from django.http import HttpResponse

def myfunction(request,):
    text = "Name: Nibha Swarup Student Id: 82312 In my Web Security class I have learnt the following: MVC framework, learnt in detail" \
           "about VPN, learnt about firewalls, routers, about the ISO and TCP/IP models. I also learnt and made project including wireframes" \
           "about the google two phase authentication. "

    return HttpResponse(text)