# Generated by Django 4.2.8 on 2024-03-29 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dab_resource_registry', '0003_alter_resource_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcetype',
            name='migrated',
        ),
    ]