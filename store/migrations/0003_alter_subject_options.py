# Generated by Django 4.0.3 on 2022-03-27 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('ordering',), 'verbose_name_plural': 'Subject'},
        ),
    ]
