# Generated by Django 4.2.3 on 2023-07-07 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='available_count',
            new_name='in_stock',
        ),
    ]
