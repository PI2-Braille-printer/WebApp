from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

sendfile_storage = FileSystemStorage(location=settings.SENDFILE_ROOT)


def default_upload_path(instance, filename):
    return 'public/{0}/'.format(filename)

class UploadFile(models.Model):
    title = models.CharField(("Title"), max_length=255)
    file = models.FileField(("Upload File"), upload_to=default_upload_path, storage=sendfile_storage)
    
    def save(self, *args, **kwargs):
        # Override file if existing
        if self.pk is not None and self.file is not None:
            self.file.delete()
            self.delete()
        super(UploadFile, self).save(*args, **kwargs)
