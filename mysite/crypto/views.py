from django.shortcuts import render

def home(request):
    import pip._vendor.requests 
    import json

    price_request= pip._vendor.requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,USDT,XLM,EOS&tsyms=USD")
    price= json.loads(price_request.content)
    

    api_request= pip._vendor.requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api= json.loads(api_request.content)
    return render(request, 'home.html', {'api':api, 'price':price})


def prices(request):
    if request.method == 'POST':
        quote= request.POST['quote']
        return render(request, 'home.html', {'quote':quote})


    else:
        return render(request, 'prices.html', {})