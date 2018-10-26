# Generated by Django 2.1.2 on 2018-10-23 17:02

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_uploadfile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to=webapp.models.default_upload_path, verbose_name='Upload File'),
        ),
    ]
