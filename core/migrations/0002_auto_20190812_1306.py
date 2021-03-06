# Generated by Django 2.2.3 on 2019-08-12 17:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfig',
            name='order_by_field',
            field=models.CharField(default='-modified_timestamp', max_length=64),
        ),
        migrations.AddField(
            model_name='appconfig',
            name='subject',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='html_form_template',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Email Template'),
        ),
    ]
