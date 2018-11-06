from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm, DefaultForm
from .models import UploadFile, Text
from django.shortcuts import get_object_or_404
import os

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
        #if not success:
            #messages.error(request, _("Failed to save!"))
        #else:
            #messages.success(request, _("Entry saved!"))
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
                form.save()
                success = True
            except Exception as e:
                success = False
                print(e)
        #if not success:
            #messages.error(request, _("Failed to save!"))
        #else:
            #messages.success(request, _("Entry saved!"))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = DefaultForm()
    return render(
        request,
        'webapp/text_form.html',
        {'form': form}
    )

def download_file(request):
    obj = get_object_or_404(UploadFile, active=True)
    file_path = obj.file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            obj.active = False
            obj.save()
            return response

def get_text(request):
    obj = get_object_or_404(Text, active=True)
    obj.active = False
    obj.save()
    return HttpResponse(obj.content)