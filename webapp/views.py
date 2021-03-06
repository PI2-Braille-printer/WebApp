from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm, DefaultForm
from .models import UploadFile, Text
from django.shortcuts import get_object_or_404
import os
from django.core.files import File
from django.contrib import messages

def index(request):
    return render(request, 'webapp/base.html')
# Create your views here.
def upload_file_form(request):
    if request.method == "POST":
        success = False
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                success = True
            except Exception as e:
                success = False
                print(e)
        if not success:
            messages.error(request, "Failed to save!")
        else:
            messages.success(request, "Entry saved!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = UploadFileForm()
    return render(
        request,
        'webapp/upload_file_form.html',
        {'form': form}
    )

def text_form(request):
    if request.method == "POST":
        success = False
        form = DefaultForm(request.POST)
        if form.is_valid():
            try:
                obj = form.save()
                myFile = None
                with open(str(obj.pk)+'.txt', 'w') as f:
                    myFile = File(f)
                    myFile.write(str(obj.content))
                f = open(str(obj.pk)+'.txt', 'r')
                myFile = File(f)
                upload_file = UploadFile(file=myFile, active=True)
                upload_file.save()
                myFile.close()
                f.close()
                print(upload_file.file.name)
                success = True
            except Exception as e:
                success = False
                print(e)
        if not success:
            messages.error(request, "Failed to save!")
        else:
            messages.success(request, "Entry saved!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = DefaultForm()
    return render(
        request,
        'webapp/text_form.html',
        {'form': form}
    )

from django.http import Http404

def download_file(request):
    try:
        obj = UploadFile.objects.filter(active=True)[0]
    except:
        raise Http404('Nao tem download')
    file_path = obj.file.path

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            obj.active = False
            obj.save()
            return response
    else:
        obj.active = False
        obj.save()
        raise Http404(str(file_path)+ ' nao encontrado')

def get_text(request):
    obj = get_object_or_404(Text, active=True)
    obj.active = False
    obj.save()
    return HttpResponse(obj.content)

def text_list(request):
    objs = Text.objects.filter(active=True)
    
    return render(request, 'webapp/text_list.html', {'objs': objs})
