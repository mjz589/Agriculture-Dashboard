# Generated by Django 4.2.1 on 2023-05-31 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_product_options_alter_project_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productstatus',
            options={'verbose_name': 'وضعیت محصول', 'verbose_name_plural': 'وضعیت محصولات'},
        ),
    ]
