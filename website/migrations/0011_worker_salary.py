# Generated by Django 4.2.1 on 2023-06-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_worker_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='salary',
            field=models.CharField(default='350000 Toman', max_length=100),
        ),
    ]