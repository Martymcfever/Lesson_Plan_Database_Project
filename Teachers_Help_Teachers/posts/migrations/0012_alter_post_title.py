# Generated by Django 5.0.6 on 2024-07-15 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_rename_is_verified_post_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
    ]