from myproject.functions import reCaptcha

@csrf_exempt
def register(response):
    if response.POST:
        if reCaptcha(response):
            pass # OK!
        else:
            pass # FAIL!
    else:
        pass 
