# Generated by Django 4.2.1 on 2023-06-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_worker_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='skill',
            field=models.CharField(default='کارگر ساده', max_length=100),
        ),
    ]
