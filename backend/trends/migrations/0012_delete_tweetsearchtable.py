# Generated by Django 2.0.5 on 2018-05-17 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0011_tweetsearchtable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TweetSearchTable',
        ),
    ]