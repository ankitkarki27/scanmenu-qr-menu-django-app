from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings
from django.http import HttpResponse
# views.py
def generate_qr_code(request):
    if request.method == 'POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name=form.cleaned_data['restaurant_name']
            url=form.cleaned_data['url']
            
            # generate the QR code
            qr = qrcode.make(url)
            file_name= restaurant_name.replace("","_").lower() + "_menu.png"
            file_path=os.path.join(settings.MEDIA.ROOT,file_name) #media/restaurant_name_menu.png
            qr.save(file_path)
            # qr.save('file_name')    
            
            context={
                'form': form,
                'qr_code': file_name,
                'restaurant_name': restaurant_name,
                'url': url,
            }
            return render(request,'your_qr.html',context)

    else:
        form=QRCodeForm()
        context={
            'form': form,
            
        }
        return render(request, 'qr_code.html', context)

