# Generated by Django 2.2.7 on 2020-04-28 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0013_auto_20200428_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='document',
            new_name='header_img',
        ),
    ]