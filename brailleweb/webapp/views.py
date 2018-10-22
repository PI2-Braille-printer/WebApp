from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm

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