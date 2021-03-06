# Generated by Django 2.2.3 on 2019-08-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190812_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appconfig',
            name='order_by_field',
            field=models.CharField(choices=[('MODIFIED_TIMESTAMP_ASC', 'modified_timestamp'), ('MODIFIED_TIMESTAMP_DESC', '-modified_timestamp'), ('VIDEO_PATH_ASC', 'video_path'), ('VIDEO_PATH_DESC', '-video_path')], default='MODIFIED_TIMESTAMP_DESC', max_length=64),
        ),
    ]
