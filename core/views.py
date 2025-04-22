from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

# views.py
def generate_qr_code(request):
    if request.method == 'POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name=form.cleaned_data['restaurant_name']
            url=form.cleaned_data['url']
            
            # generate the QR code
            qr = qrcode.make(url)
            print(qr)
        
            #save
            qr.save('test_qr.png')            
    else:
        form=QRCodeForm()
        context={
            'form': form,
        }
    
        return render(request, 'qr_code.html', context)

