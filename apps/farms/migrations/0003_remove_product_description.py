# Generated by Django 3.2.4 on 2021-08-27 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0002_alter_contact_whatsapp_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]