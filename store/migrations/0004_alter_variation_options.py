# Generated by Django 4.0.4 on 2022-05-25 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_variations_variation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variation',
            options={'ordering': ['variation_category']},
        ),
    ]