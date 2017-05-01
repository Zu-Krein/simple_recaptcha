# simple_recaptcha

If the key is fine, then `True`

If Google did not like the key - `False`


> Example for `Django`:

* `Copy` the file to the `project folder`.

* Next, go to `views.py`

```python
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
	```
