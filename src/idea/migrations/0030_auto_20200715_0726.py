# Generated by Django 2.2.7 on 2020-07-15 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0029_idea_notified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idea',
            options={'ordering': ['-id']},
        ),
    ]