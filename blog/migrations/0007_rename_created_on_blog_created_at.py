# Generated by Django 5.0.4 on 2024-04-16 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created_on',
            new_name='created_at',
        ),
    ]