# Generated by Django 2.0.5 on 2018-05-17 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0014_delete_tweetsearchtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetSearchTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data', models.CharField(max_length=255)),
                ('tid', models.TextField(null=True)),
                ('retweet', models.TextField(null=True)),
                ('favorite_count', models.TextField(null=True)),
                ('uname', models.TextField(null=True)),
                ('profimg', models.TextField(null=True)),
                ('query1', models.TextField(null=True)),
            ],
            options={
                'db_table': 'tweetsearch_table',
                'managed': True,
            },
        ),
    ]
