# Generated by Django 4.2 on 2023-06-24 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0003_post_pic"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="pic",),
    ]
