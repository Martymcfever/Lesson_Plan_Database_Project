# Generated by Django 5.0.6 on 2024-07-12 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
