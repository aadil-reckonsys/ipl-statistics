# Generated by Django 2.2.6 on 2019-11-02 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20191102_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='match_id',
            new_name='match',
        ),
    ]