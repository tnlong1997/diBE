# Generated by Django 2.0 on 2017-12-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dibe', '0003_auto_20171223_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='host_ids',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='share_ids',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=300),
        ),
    ]
