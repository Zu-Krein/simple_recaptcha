from settings import RECAPTCHA_PRIVATE_KEY, ALLOWED_HOSTS
import urllib.request, json

def getIp(response):
    directional = response.META.get('HTTP_X_FORWARDED_FOR')
    if directional:
        IP = directional.split(',')[0]
    else:
        IP = response.META.get('REMOTE_ADDR')
    return IP

def reCaptcha(response):
    if response.POST:
        if not response.POST.get('g-recaptcha-response', ''):
            return False
        url = 'https://www.google.com/recaptcha/api/siteverify'
        re = response.POST.get('g-recaptcha-response', '')
        ip = get_client_ip(response)
        url_date = url + '?secret=' + RECAPTCHA_PRIVATE_KEY + '&response=' + re + '&remoteip=' + ip
        with urllib.request.urlopen(url_date) as response:
            html = response.read().decode('utf8')
        result = json.loads(html)
        if result['success'] and result['hostname'] in ALLOWED_HOSTS:
            return True
        else:
            return False
    else:
        return False 
